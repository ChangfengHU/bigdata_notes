//http模块用来创建http服务实例
var http = require("http");

//fs模块用来读写文件
var fs = require("fs");

//path模块可以用来拼接路径字符串
var path = require("path");

//mime模块可以根据文件名来判断当前文件的Content-Type
var mime = require("mime");

//url模块可以提供一个方法 用来解析url地址的
var url = require("url");

var server = http.createServer();

server.on("request", function (req, res) {

    res.render = function (filename) {
        fs.readFile(filename, (err, data) => {
            if (err) {
                this.writeHead(404, "Not Found", {
                    "Content-Type": "text/html;charset=utf-8"
                })
                this.end("<h1>您访问的页面不存在</h1>")
            }
            this.writeHead(200, "OK", {
                "Content-Type": mime.getType(filename)
            })
            this.end(data);
        })
    }

    if ((req.url == "/" || req.url == "/index") && req.method == "GET") {
        res.readFile(path.join(__dirname, "views/index.html"),res);
    } else if (req.url == "/details" && req.method == "GET") {
        res.render(path.join(__dirname, "views/details.html"));
    } else if (req.url == "/publish" && req.method == "GET") {
        res.render(path.join(__dirname, "views/submit.html"));
    } else if (req.url.startsWith("/resources") && req.method == "GET") {
        res.render(path.join(__dirname, req.url));
    } else if (req.url.startsWith("/add") && req.method == "GET") {
        var news = url.parse(req.url, true).query;
        var newsArr;
        //1. 获取之前已经存储过的新闻数据（读文件）
        fs.readFile(path.join(__dirname, "data.json"), "utf-8", function (err, data) {
            if (err) {
                newsArr = [];
            } else {
                newsArr = JSON.parse(data);
            }
            // 将用户提交的数据存储到data.json文件中
            newsArr.push(news);
            //将存储新闻的数组，写入的data.json文件中
            fs.writeFile(path.join(__dirname, "data.json"), JSON.stringify(newsArr), function (err) {
                if (err) {
                    res.writeHead(500, "内部服务器错误", {
                        "Content-Type": "text/html;charset=utf-8"
                    })
                    res.end("文件写入失败！！");
                }
                res.statusCode = 302;
                res.statusMessage = "Found";
                res.setHeader("Location", "/");
                res.end();
            })
        })
        // res.end("请求成功")
    } else {
        res.writeHead(404, "Not Found", {
            "Content-Type": "text/html;charset=utf-8"
        })
        res.end("<h1>您访问的页面不存在</h1>")
    }

})


server.listen(8080, function () {
    console.log("Hacker-News已经运行在 http://localhost:8080")
})

function readFile(fileName, response) {
    fs.readFile(fileName, function (err, data) {
        if (err) {
            throw err
        }
        response.end(data)
    })
}










//rest参数
// var sum = (...arr)=>{

// }

// sum(1,2,3,34,5,5,6,6,6)
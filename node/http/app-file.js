var http = require("http");
var server = http.createServer();
var fs = require("fs");
var path = require("path");

server.on("request", function(request, response){

    response.writeHead(200, "OK", {
        "Content-Type": "text/html;charset=utf-8"
    })
    

    //浏览器中的url地址，其实只是一个标识符，这个标识符是由后台程序处理之后，会返回相应的结果
    //之前，我们之所以可以通过路径访问到对应的文件，是由apache自己做的处理
    //现在我们不用apache了，而是自己使用node来实现apache的功能
    //所以，我们需要自己通过node.js中的代码 分析用户要请求的内容，然后通过代码将用户要请求的文件找到之后返回给用户

    console.log(request.url);

    if(request.url == "/shuaige"){
        //可以使用fs 读取views下面的html页面，将其内容返回给浏览器
        fs.readFile(path.join(__dirname, "views/shuaige.html"), "utf-8", function(err, data){
            if(err){
                throw err;
            }

            //end方法，可以结束响应，并且可以传递参数，将参数中的内容加到响应体中
            response.end(data);
        })
       
    }else if(request.url == "/meinv/qqq/www/eee"){
        fs.readFile(path.join(__dirname, "views/meinv.html"), "utf-8", function(err, data){
            if(err){
                throw err;
            }

            //end方法，可以结束响应，并且可以传递参数，将参数中的内容加到响应体中
            response.end(data);
        })
    }else if(request.url == "/yeshou"){
        fs.readFile(path.join(__dirname, "views/yeshou.html"), "utf-8", function(err, data){
            if(err){
                throw err;
            }

            //end方法，可以结束响应，并且可以传递参数，将参数中的内容加到响应体中
            response.end(data);
        })
    }else if(request.url == "/meinv/qqq/www/imgs11"){
        fs.readFile(path.join(__dirname, "/imgs/timg.jpg"), function(err, data){
            if(err){
                throw err;
            }

            response.end(data);
        })
    }else if(request.url == "/meinv/qqq/www/css/base.css"){

        response.writeHead(200,"ok",{
            "Content-Type":"text/css;charset=utf-8"
        })
        fs.readFile(path.join(__dirname, "/css/base.css"), function(err, data){
            if(err){
                throw err;
            }

            response.end(data);
        })
    }else{
        response.writeHead(404, "Not Found", {
            "Content-Type": "text/html;charset=utf-8"
        })
        response.write("<h1>这个页面丢了！！</h1>")
    }
})

//4. 开启http服务的监听，准备接收请求
server.listen("8083", function(){
    console.log("服务器已经开启，监听端口为8080， 请访问:http://localhost:8080")
})

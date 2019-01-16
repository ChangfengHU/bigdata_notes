var http = require("http")
var fs = require("fs")
var path = require("path")
var service = http.createServer()
service.on("request", function (request, response) {
    console.log(request.url);
    response.writeHead(200, "ok", {
        "Content-Type": "text/html;charset=utf-8"
    })
    response.end("我接收到请求了")
})
service.listen(8085, function () {
    console.log("服务器开启成功");
})

function readFile(fileName, response) {
    fs.readFile(path.join(__dirname, fileName), function (err, data) {
        if (err) {
            throw err
        }
        response.end(data)
    })
}
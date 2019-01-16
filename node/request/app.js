import { SSL_OP_ALL } from "constants";

var http = require("http")
var fs = require("fs")
var path = require("path")
var mime = require("mime")
var service = http.createServer()
service.on("request", function (request, response) {
    console.log(request.url);

SSL_OP_ALLss

dddd 
    response.writeHead(200, "ok", {
        "Content-Type": "text/html;charset=utf-8"
    })
    // if (request.url == "/" || request.url == "/index.html") {
    //     readFile("public/index.html",response)
    // } else if(request.url.indexOf("/public")==0){
    //     console.log(2123);

    //     response.writeHead(200, "ok", {
    //         "Content-Type": mime.getType(request.url)+";charset=utf-8"
    //     })
    //     readFile(request.url,response)
    // } else {
    //     response.writeHead(404, "Not1 Fount", { 
    //         "Content-Type": "text/html;charset=utf-8"
    //     })
    //     response.end("<h1>页面找不到了</h1>")
    // }

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
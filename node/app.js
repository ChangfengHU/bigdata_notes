//1. 引入http模块
var http = require("http");

//2. 通过http模块提供的createServer方法，创建出来一个http服务实例
var server = http.createServer();
//3.add request to service handle thing
//request have two param, request respond 
//when server is 
server.on("request",function(request,response){
    console.log("somebody come on");
    console.log(request.url);
    response.writeHead(200, "OK", {
        "Content-Type": "text/html;charset=utf-8",
        "name": "pm"
    });
    if(request.url=="/home"){
        response.write("<String> home页面 </String>")
    }
    if(request.url=="/list"){
        response.write("<String> list页面 </String>")
    }
    response.end();
})
//4.open httpservice and open listene
server.listen("8081",function  () {
    console.log("listen start...");
    
} )
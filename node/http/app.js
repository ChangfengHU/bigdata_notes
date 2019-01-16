//1. 引入http模块
var http = require("http");

//2. 通过http模块提供的createServer方法，创建出来一个http服务实例
var server = http.createServer();

//3. 为http服务注册一个处理请求事件的事件处理函数

//request事件处理函数中，有两个形参， request response
//当有请求发送给当前服务实例的时候，这个事件会被触发，nodejs会调用事件处理函数

//并且将当前请求所有的请求相关的信息全部放到request中
//将所有和响应相关的内容，放到response中
server.on("request", function(request, response){
    //request.url可以用来获取当前浏览器所请求的地址
    console.log(request.url);

    //我们可以通过判断用户所访问的url 来返回不同的内容

    // response.writeHead(200, "OK", {
    //     "Content-Type": "text/html;charset=utf-8"
    // })

    // response.statusCode = 404;
    // response.statusMessage = "Not Found";
    // response.setHeader("Content-Type", "text/html;charset=utf-8")


    response.writeHead(200, "OK", {
        "Content-Type": "text/html;charset=utf-8"
    })

    if(request.url == "/shuaige"){
        response.write("<h1>这里是帅哥页面</h1><div style='background-color: hotpink;'>home hello谈海银</div>")
    }else if(request.url == "/meinv"){
        response.write("<h1>这里是美女页面</h1><div style='background-color: hotpink;'>home hello戴卫芳</div>")        
    }else if(request.url == "/yeshou"){
        response.write("<h1>这里是野兽页面</h1><div style='background-color: hotpink;'>home hello 朱小俊</div>")
    }else{
        response.writeHead(404, "Not Found", {
            "Content-Type": "text/html;charset=utf-8"
        })
        response.write("<h1>这个页面丢了！！</h1>")
    }

    response.end();
})

//4. 开启http服务的监听，准备接收请求
server.listen("8080", function(){
    console.log("服务器已经开启，监听端口为8080， 请访问:http://localhost:8080")
})

###Django基础必备三神装（HttpResponse、render,、redirect）
````2018年06月12日 17:01:36 miaoqinian 阅读数：6592
在使用三神装的时候，首先当然是得要导入它们：

from django.shortcuts import HttpResponse, render, redirect
1.HttpResponse

它是作用是内部传入一个字符串参数，然后发给浏览器。

例如：

def index(request):
    # 业务逻辑代码
    return HttpResponse("OK")
2、render

render方法可接收三个参数，一是request参数，二是待渲染的html模板文件,三是保存具体数据的字典参数。

它的作用就是将数据填充进模板文件，最后把结果返回给浏览器。与jinja2类似。

例如：

def index(request):
    # 业务逻辑代码
    return render(request, "index.html", {"name": "monicx", "hobby": ["reading", "blog"]})
3、redirect

接受一个URL参数，表示让浏览器跳转去指定的URL.

例如：

def index(request):
    # 业务逻辑代码
    return redirect("https://blog.csdn.net/miaoqinian")
    
````    
    
###  linux生成django

1.安装 Djangopip install django
2.创建 Django 工程 django-admin startproject djangoproject
3.django-admin startapp search
4.初始化项目 python3 manage.py migrate
5.启动项目python3 manage.py runserver 0.0.0.0:8080
nohup python manage.py runserver 0.0.0.0 8080 &

###连接es
client = Elasticsearch(
        ['47.97.247.78'],
        http_auth=('elastic', '36yes58no!@#'),
        port=9200
)


connections.create_connection(
                           hosts=["47.97.247.78"], 
                           http_auth=('elastic', '36yes58no!@#'),
                           port=9200,
                           timeout=20)
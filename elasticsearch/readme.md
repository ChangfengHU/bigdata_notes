## 本地开启
1.开启es

D:\work\elasticsearch-5.1.1\bin

 .\elasticsearch.bat

访问 ：http://127.0.0.1:9200/
2.开启head
1.git bash
2.npm start
3. 访问http://127.0.0.1:9100/


3.开启 kibana

D:\work\kibana-5.1.2-windows-x86\bin
kibana.bat
访问:http://127.0.0.1:5601/app/kibana#/management/kibana/index/?_g=()

###下载软件网址
- 下载 es：官网 https://www.elastic.co/downloads/past-releases
版本 5.1.1

- 下载 kibana：官网 https://www.elastic.co/downloads/past-releases  
下载对应版本 5.1.1

- 下载 head  ：https://github.com/mobz/elasticsearch-head



下载 elasticsearch-dsl : pip install elasticsearch-dsl

 官网:https://elasticsearch-dsl.readthedocs.io/en/latest/

- es深入学习网站 https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html

- 爬虫抢票深入学习网站
https://github.com/Jack-Cherish/python-spider



- linux安装 es

参考网站
chown -R elasticUser:elasticUser /data/elasticsearch-6.2.4
http://ju.outofmemory.cn/entry/358335
启动错误
https://www.2cto.com/net/201706/650950.html

su elasticUser

elasticUser       hard        nofile        65536
elasticUser       soft        nofile        65536

关闭es
ps -ef | grep elastic
kill -9  41565
测试分词
curl -H "Content-Type: application/json" 'http://127.0.0.1:9200/jobbole/_analyze?pretty=true' -d '{"text":"这里是好记性不如烂笔头感叹号的博客园"}'

ik分析相关

https://github.com/medcl/elasticsearch-analysis-ik/releases?after=v6.3.2 


- linux安装 anaconda 
https://www.cnblogs.com/hdulzt/p/7156095.html

一键安装 ik分词
./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.2.4/elasticsearch-analysis-ik-6.2.4.zip

cur es操作模板
curl -XPUT http://localhost:9200/jobbole1
curl -XPOST http://localhost:9200/jobbole1/article/_mapping -H 'Content-Type:application/json' -d'
{
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_max_word"
            }
        }

}'

GET _all

curl -XPOST http://localhost:9200/jobbole1/article/1 -H 'Content-Type:application/json' -d'
{"content":"美国留给伊拉克的是个烂摊子吗"}
'
curl -XPOST http://localhost:9200/jobbole1/article/2 -H 'Content-Type:application/json' -d'
{"content":"公安部：各地校车将享最高路权"}
'
curl -XPOST http://localhost:9200/jobbole1/article/3 -H 'Content-Type:application/json' -d'
{"content":"中韩渔警冲突调查：韩警平均每天扣1艘中国渔船"}
'
curl -XPOST http://localhost:9200/jobbole1/article/4 -H 'Content-Type:application/json' -d'
{"content":"中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首"}
'

curl -XPOST http://localhost:9200/jobbole1/article/_search  -H 'Content-Type:application/json' -d'
{
    "query" : { "match" : { "content" : "python" }},
    "highlight" : {
        "pre_tags" : ["<tag1>", "<tag2>"],
        "post_tags" : ["</tag1>", "</tag2>"],
        "fields" : {
            "content" : {}
        }
    }
}
'



1.查询索引下mapping的信息

 curl -XGET http://localhost:9200/jobbole1/_mapping?pretty

2 .查询索引下settting的信息

curl -XGET http://localhost:9200/jobbole1/_settings?pretty

## bool 查询
- "filter":[] 
- "must":[]  and
- "should":[] or
- "must_not":[] not

### -批量插入数据

````
POST boss/testjob/_bulk
{"index":{"_id":"1"}}
{"salary":2,"title":"Python"}
{"index":{"_id":"2"}}
{"salary":6,"title":"Scarpy"}
{"index":{"_id":"3"}}
{"salary":8,"title":"Java"}
{"index":{"_id":"4"}}
{"salary":14,"title":"Django"}
{"index":{"_id":"5"}}
{"salary":16,"title":"Elasticsearch"}
{"index":{"_id":"6"}}
{"salary":1,"title":"scala"}
````


### - 简单过滤查询
- select * from testjob where salary = 20
- 薪资为8k的工作
````
GET lagou/testjob/_search
{
   "query":
   {
    "bool":{
      "must":{
        "match_all":{}
      },
      "filter":{
         "term":{
           "salary":20
         }
      }
    }
   }
}

````
````
GET boss/testjob/_search
{
   "query":
   {
    "bool":{
      "must":{
        "match_all":{}
      },
      "filter":{
         "terms":{
           "salary":[8,2]
         }
      }
    }
   }
}

````
### - 简单过滤查询1
- match和term区别
- elasticsearch如果不设置index=false 
就会进行倒排索引,term查询查不到,match查询就能才查到
或者查询纯小写
````
GET boss/testjob/_search
{
 "query":{ 
     "bool":{
      "filter":{
         "term":{
           "title":"elasticsearch"
         }
      }
    }
 }
}
````
````
GET boss/testjob/_search
{
 "query":{ 
     "bool":{
      "filter":{
         "match":{
           "title":"Elasticsearch"
         }
      }
    }
 }
}
````
### - 查询分析器分析的结果
````
GET _analyze 
{
   "analyzer": "ik_max_word",
   "text":"研究员wangzhan"
}
````
- 结果
````
{
  "tokens": [
    {
      "token": "研究员",
      "start_offset": 0,
      "end_offset": 3,
      "type": "CN_WORD",
      "position": 0
    },
    {
      "token": "研究",
      "start_offset": 0,
      "end_offset": 2,
      "type": "CN_WORD",
      "position": 1
    },
    {
      "token": "员",
      "start_offset": 2,
      "end_offset": 3,
      "type": "CN_CHAR",
      "position": 2
    },
    {
      "token": "wangzhan",
      "start_offset": 3,
      "end_offset": 11,
      "type": "ENGLISH",
      "position": 3
    }
  ]
}
 
````

### - 组合查询
- 组合查询
- select *from testjob where (salary=8 OR
title =java
) AND (salary !=30)
````
GET boss/testjob/_search
{
  "query": {
    "bool": {
      "should": [
        {"term": {"salary": 8}},
        {"term": {"title": "java"}}
      ]
      , "must_not": [
        {"term": {
          "salary": 30
        }}
      ]
    }
  }
  
}

````

### - 嵌套查询

- select *from testjob where title =java or (salary=14 and title =django) AND (salary !=9)
GET boss/testjob/_search
{
  "query": {
    "bool": {
      "should": [
        {"term": {"title": "java"}},
        {"bool": {
          "must": [
            {"term": {"salary": 14}},
             {"term": {"title": "django"}}
          ]
          
        }}
        
      ]
      , "must_not": [
        {"term": {
          "salary": 9
        }}
      ]
    }
  }
  
}
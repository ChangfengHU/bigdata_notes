
## 索引库的映射
- 创建索引的时候，定义字段类型  
##### 内置类型
- string类型：text，keyword
- 数字类型：long，integer
- 日期类型：data
- 复杂类型：object，nested
object：就是一个json对象，
nested，就是一个数组
##### 创建映射
````
PUT lagou
{
"mappings":{
 "job":{
  "properties":{
  "title":{
    "type":"text"
  },
  "salary_min":{
    "type":"integer"
  },
  "city":{
    "type":"keyword"
  },
  "company":{
    "properties":{
        "name":{
            "type":"text"
        },
    
        "company_adder":{
            "type":"text"
        },
        "employee_count":{
            "type":"integer"
        }
    
    
    }
  },
  "publish_date":{
    "type":"date",
    "format":"yyyy-MM-dd"
  },
  "comments":{
    "type":"integer",
  }
  }
 }
}
}
````
##### 创建映射数据
````
PUT lagou/job/1
{
    "title":"python分布式爬虫开发",
    "salary_min":124,
    "city":"北京",
    "company":{
        "name":"百度",
        "company_adder":"北京市软件园",
        "employee_count":50
    },
    "publish_date":"2017-4-18",
    "comments":15
}
````

##### 创建映射2
````
PUT spiderdata
{
"mappings":{
 "IT":{
  "properties":{
  "positionName":{
    "store":"true",
    "type":"text",
    "analyzer":"ik_max_word"
  },
  "positionLink":{
    "type":"text"
  },
  "positionType":{
    "type":"keyword"
  },
  "peopleNumber":{
    "type":"integer"
  },
  "workLocation":{
    "store":"true",
    "type":"keyword"
  },
  "publishTime":{
    "type":"date",
    "format":"yyyy-MM-dd"
  }
  }
 }
}
}
````

##### 创建映射2数据
````
PUT spiderdata/IT/
{"positionName": "CSIG16-手图运营开发工程师（北京）", "positionLink": "position_detail.php?id=36510&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "1", "workLocation": "北京", "publishTime_date": "2018-11-13"}

POST spiderdata/IT/
{"positionName": "20503-计算机视觉高级研究员（深圳）", "positionLink": "position_detail.php?id=36488&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "1", "workLocation": "深圳", "publishTime": "2018-11-13"}




````
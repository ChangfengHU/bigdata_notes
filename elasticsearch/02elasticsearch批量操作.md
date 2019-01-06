
##索引库的批量查询
- 查询
##### 批量查询多条数据
- 使用 mget
- 不同索引库
````
GET _mget 
{
"docs":
[
  {
  "_index":"music",
  "_type":"IT",
  "_id":1
  },
  {
  "_index":"douyu",
  "_type":"image",
  "_id":2
    
  }
    ]
}

````

##### 批量查询多条数据
- 同一索引不同type表

````
GET music/_mget 
{
"docs":
[
  {
  "_type":"IT",
  "_id":1
  },
  {
  "_type":"IT",
  "_id":2
    
  }
    ]
}
````

##### 批量查询多条数据
- 同一索引库同一type表

````
GET music/IT/_mget 
{
"docs":
[
  {
  "_id":1
  },
  {
  "_id":2
  }
    ]
}
````
- 简写方式
GET music/IT/_mget 
{
"ids":[1,2]
}


##索引库的批量操作
- 增加
- 更新
- 删除

##### 批量插入多条数据
- 使用_bulk
````
POST _bulk
{"index":{"_index":"music","_type":"IT","_id":"4"}}
{"positionName": "22850-腾讯视频VIP积分商城产品经理（深圳）", "positionLink": "position_detail.php?id=36571&keywords=&tid=0&lid=0", "positionType": "产品/项目类", "peopleNumber": "1", "workLocation": "深圳", "publishTime": "2018-11-13"}
{"index":{"_index":"music","_type":"IT","_id":"5"}}
{"positionName": "25923-数据分析师（深圳）", "positionLink": "position_detail.php?id=36592&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "1", "workLocation": "深圳", "publishTime": "2018-11-13"}
````

##### 批量更新多条数据
````
POST _bulk
{"update":{"_index":"music","_type":"IT","_id":"4"}}
{"doc":{"workLocation": "杭州1", "publishTime": "2019-11-11"}}
{"update":{"_index":"music","_type":"IT","_id":"5"}}
{"doc":{"workLocation": "杭州1", "publishTime": "2019-11-13"}}

````
##### 批量删除多条数据

{"delete":{"_index":"music","_type":"IT","_id":"4"}}
{"delete":{"_index":"music","_type":"IT","_id":"5"}}
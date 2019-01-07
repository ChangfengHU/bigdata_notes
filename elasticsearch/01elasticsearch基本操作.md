index--type-- 
## 索引库的增删改查
##### 1.创建一个索引库

- 一旦创建分片数量不能修改    
````
PUT music
{
  "settings": {
    "index" : {  
      "number_of_shards":5,
      "number_of_replicas":1
    }
  }
}
````
##### -查询索引的settings
```
GET music/_settings
```
##### - 修改索引settings
```
PUT music/_settings
{
 "number_of_replicas":1
}
```

##### - 获取所有索引settings
   ```
   GET _all
   
   ```
##### - 获取所有索引settings
```
GET _all

```    
## 索引库文章的增删改查
##### - 创建文章一条数据
- 指明id 使用put
````
PUT music/IT/3
{"positionName": "22850-腾讯视频VIP后台开发", "positionLink": "position_detail.php?id=36569&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "1", "workLocation": "深圳", "publishTime": "2018-11-13"}
````
##### - 创建文章一条数据
- 不指明id 使用post
````
POST music/IT/
{
"positionName": "PCG19-腾讯视频自然语言处理高级工程师（北京）", "positionLink": "position_detail.php?id=36566&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "2", "workLocation": "北京", "publishTime": "2018-11-13"
}
````

##### - 查看文章一条数据
- 整条数据
````
GET music/IT/1

````
##### - 查看文章一条数据
- 某些字段
````
GET music/IT/1?_source=positionName,positionType

````    
##### - 修改文章一条数据
- 覆盖修改 使用put
````
PUT music/IT/1
{
"positionName": "25923-机器学习平台研发工程师（深圳）", "positionLink": "position_detail.php?id=36593&keywords=&tid=0&lid=0", "positionType": "技术类", "peopleNumber": "2", "workLocation": "杭州", "publishTime": "2018-11-13"
}
````
##### - 修改文章一条数据
- 指定修改 使用post

````
POST music/IT/1/_update
{
"doc":{
"positionType": "管理类"
  }
}
````
##### - 删除文章一条数据
````
 delete music/IT/1
````

##### - 删除文章一张表
````
 delete music/IT
````


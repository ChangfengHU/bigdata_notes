## bool 查询
- "filter":[]
- "must":[]
- "should":[]
- "must_not":[]

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
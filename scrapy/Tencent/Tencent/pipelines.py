# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#方案0
import json
from scrapy.exporters import JsonItemExporter
class MinePipeline(object):
    def __init__(self):
        self.f = open("data\\jobbole1.json", "w")
    def process_item(self, item, spider):
        #dicq = eval(str(item))
        print(spider.name)
        temp = {}
        content = json.dumps(dict(eval(str(item))), ensure_ascii=False)+",\n"
        self.f.write(content)
        print(content)
        return item

    def close_spider(self, spider):
        self.f.close()
#方案一
# import json
# from scrapy.exporters import JsonItemExporter
# class TencentPipeline(object):
#     def __init__(self):
#         self.f = open("D:\\spark-input\\tencent2.json", "w")
#     def process_item(self, item, spider):
#         #dicq = eval(str(item))
#         print(spider.name)
#         temp = {}
#         if  spider.name=="duanzi":
#             temp['author'] = item["author"]
#             temp['content'] = item["content"]
#         if spider.name == "tencent":
#             temp['positionName'] =str(item["positionName"], encoding='utf-8')
#             temp['positionLink'] =str(item["positionLink"], encoding='utf-8')
#             temp['positionType'] =str(item["positionType"], encoding='utf-8')
#             temp['peopleNumber'] =str(item["peopleNumber"], encoding='utf-8')
#             temp['workLocation'] =str(item["workLocation"], encoding='utf-8')
#             temp['publishTime'] =str(item["publishTime"], encoding='utf-8')
#         content = json.dumps(temp, ensure_ascii=False)+",\n"
#         self.f.write(content)
#         print(content)
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()


##方案二
# import json
# from scrapy.exporters import JsonItemExporter
# class TencentPipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
#         self.exporter.start_exporting()
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了")



# ##方案三
import json
from scrapy.exporters import JsonLinesItemExporter
class TencentPipeline(object):
    def __init__(self):
        # self.fp = open("D:\\spark-input\\kugouMusic.json", "wb")
        self.fp = open("data\\jobbole.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def close_spider(self, spider):
        print("爬虫开始了")
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了")


from urllib import request
import os
import scrapy
from Tencent.settings import IMAGES_STORE as images_store
from Tencent.settings import IMAGES_STORE_GIRLS as images_store_girls
from Tencent.settings import IMAGES_STORE_JOBBOLE as images_store_jobbole
from scrapy.pipelines.images import ImagesPipeline
class DouyuImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_link = item['front_image_url']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        # print (results)
        # print ("*" * 30)
        # 取出results里图片信息中的 图片路径的值
        image_path = [x["path"] for ok, x in results if ok]
        name=str(item["nickname"])
        os.rename(images_store+ image_path[0], images_store_girls + name + ".jpg")
        return item

class JobboleImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['front_image_url'][0]
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        # print (results)
        # print ("*" * 30)
        # 取出results里图片信息中的 图片路径的值
        name=str(item["title"])
        image_path = [x["path"] for ok, x in results if ok]
        os.rename(images_store + image_path[0], images_store_jobbole + name + ".jpg")
        return item

class JobboleImagePipeline1(object):

    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['tags']
        category_path=os.path.join(self.path,category)
        urls = item['front_image_url']
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = item['title']+".jpg"
            request.urlretrieve(url, os.path.join(category_path, image_name))
        return item
class BMW5Pipeline(object):

    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['category']
        category_path=os.path.join(self.path,category)
        urls = item['image_urls']
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = url.split('_')[-1]
            request.urlretrieve(url, os.path.join(category_path, image_name))
        return item
import pymysql
import time
from twisted.enterprise import adbapi
from pymysql import cursors
class mysqlPipline(object):
    def __init__(self):
        dbparam={
            "host":"127.0.0.1",
            "port":3306,
            "user":"root",
            "password":"123456789",
            "database":"jianshu",
            "charset":"utf8"
        }
        self.conn=pymysql.connect(**dbparam)
        self.cursor=  self.conn.cursor()
        self._sql=None
    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
        self.conn.commit()

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into article(id,gmt_time,gmt_name,creat_time,creat_name,title,content,author,avatar,pub_time,origin_url,article_id) VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql


class mysqlPoolPipline(object):
    def __init__(self):
        dbparam = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456789",
            "database": "jianshu",
            "charset": "utf8",
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**dbparam)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
              insert into article(id,gmt_time,gmt_name,creat_time,creat_name,title,content,author,avatar,pub_time,origin_url,article_id) VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
               """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer=self.dbpool.runInteraction(self.insert_item,item)
        defer.addCallback(self.handle_error,item,spider)

    def insert_item(self,cursor,item):
        time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(self.sql,(time_now,"admin",time_now,"admin",item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
    def handle_error(self,error,item,spider):
        print("="*10+"error"+"="*10)
        print(error)
        print("=" * 10 + "error" + "=" * 10)


class jobboleMysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        dbparam = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456789",
            "database": "jianshu",
            "charset": "utf8"
        }
        self.conn = pymysql.connect(**dbparam)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        self.conn.commit()



class jobbolemysqlPoolPipline(object):
    def __init__(self):
        dbparam = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456789",
            "database": "jianshu",
            "charset": "utf8",
            'cursorclass':cursors.DictCursor
        }
        self.dbpool=adbapi.ConnectionPool('pymysql',**dbparam)
    def handle_error(self,error,item,spider):
        print("="*10+"error"+"="*10)
        print(error)
        print("=" * 10 + "error" + "=" * 10)
    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常
    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        print(insert_sql, params)
        cursor.execute(insert_sql, params)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TencentItem(scrapy.Item):
    #职位名
    positionName = scrapy.Field()

    #职位详情连接
    positionLink = scrapy.Field()

    #职位类别
    positionType = scrapy.Field()

    #招聘人数
    peopleNumber = scrapy.Field()

    #工作地点
    workLocation = scrapy.Field()

    #发布时间
    publishTime = scrapy.Field()


class QsbkItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()

class DouyuItem(scrapy.Item):
    # 主播昵称
    nickname = scrapy.Field()
    # 图片链接
    imagelink = scrapy.Field()

class BmwItem(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()
#   item =ArticleItem(title=title,avatar=avatar,author=author,pub_time=pub_time,article_id=article_id,content=content,origin_url=response.url)


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    avatar = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    pub_time = scrapy.Field()
    article_id = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()

class KugouMusicItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()

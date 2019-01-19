# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from Tencent.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT
from w3lib.html import remove_tags
import scrapy
import datetime
import re
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
    pub_time = scrapy.Field()
    article_id = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()

class KugouMusicItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()





def add_jobbole(value):
    return value+"-bobby"


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def return_value(value):
    return value


def remove_comment_tags(value):
    #去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums, front_image_url, front_image_path,
            praise_nums, comment_nums, tags)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE fav_nums=fav_nums+1
        """

        fron_image_url = ""
        front_image_path = ""
        # content = remove_tags(self["content"])

        if self["front_image_url"]:
            fron_image_url = self["front_image_url"][0]
        params = (self["title"], self["url"], self["create_date"], self["fav_nums"],
                  fron_image_url, front_image_path, self["praise_nums"], self["comment_nums"],
                  self["tags"])
        return insert_sql, params
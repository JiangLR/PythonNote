# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date


def return_value(value):
    return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0


def remove_comment_tags(value):
    # 去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 创建时间
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    # 当前页面的url
    url = scrapy.Field()
    # URL对应的MD5
    url_object_id = scrapy.Field()
    # 封面图
    front_image_url = scrapy.Field()
    # 封面图本地存放路径
    front_image_path = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    # 点赞数
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    # 评论数
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    # 收藏数
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    # 标签
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    # 内容
    content = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into article(title, url, create_date, fav_nums, front_image_url, front_image_path,
            praise_nums, comment_nums, tags, content)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
        """

        front_image_url = ""
        # content = remove_tags(self["content"])

        if self["front_image_url"]:
            front_image_url = self["front_image_url"][0]
        params = (self["title"], self["url"], self["create_date"], self["fav_nums"],
                  front_image_url, self["front_image_path"], self["praise_nums"], self["comment_nums"],
                  self["tags"], self["content"])
        return insert_sql, params

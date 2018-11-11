# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 创建时间
    create_date = scrapy.Field()
    # 当前页面的url
    url = scrapy.Field()
    # URL对应的MD5
    url_object_id = scrapy.Field()
    # 封面图
    front_image_url = scrapy.Field()
    # 封面图本地存放路径
    front_image_path = scrapy.Field()
    # 点赞数
    praise_nums = scrapy.Field()
    # 评论数
    comment_nums = scrapy.Field()
    # 收藏数
    fav_nums = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 内容
    content = scrapy.Field()
    pass

# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1.获取文章列表页中的文章url并交给解析函数进行具体字段解析
        2.获取下一页的url并交给scrapy进行下载

        :param response:
        :return:
        """
        print(response.url)
        # 获取文章列表页中的文章url并交给解析函数(parse_detail)进行具体字段解析
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            print(response.url + post_url)
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载(此时的回调函数不是parse_detail了，而是parse，因为此时的next_url为列表页，不是详情页)
        next_url = response.css('.next.page-numbers::attr(href)').extract()
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 提取文章具体字段

        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()

        create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0]. \
            strip().replace('·', '').strip()

        praise_num = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        fav_num = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', fav_num)
        if match_re:
            fav_num = int(match_re.group(1))
        else:
            fav_num = 0

        comments_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', comments_num)
        if match_re:
            comments_num = int(match_re.group(1))
        else:
            comments_num = 0

        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)
        pass

# -*- coding: utf-8 -*-
import re
import scrapy

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114493/']

    def parse(self, response):
        # 提取文章具体字段

        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")

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

        content = response.xpath("//div[@class='entry']").extract()[0]

        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)

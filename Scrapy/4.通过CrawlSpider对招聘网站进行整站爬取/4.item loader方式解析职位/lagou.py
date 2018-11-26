# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ArticleSpider.items import LagouJobItemLoader
from ArticleSpider.items import LagouJobItem
from ArticleSpider.utils.common import get_md5
import datetime


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    custom_settings = {
        'COOKIES_ENABLED': False,
        'DOWNLOAD_DELAY': 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'Cookie': "JSESSIONID=ABAAABAAAGGABCB694EBEC9C77DF785BB096A253550FCDC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543210509; _ga=GA1.2.2103576957.1543210509; _gat=1; user_trace_token=20181126133513-0c102530-f13d-11e8-8bfb-5254005c3644; LGSID=20181126133513-0c10274d-f13d-11e8-8bfb-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20181126133513-0c102908-f13d-11e8-8bfb-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_company; X_HTTP_TOKEN=82646753083ea8f79403bcf49217034d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221674e8508edd7-06c7f3cb02379c-4313362-2073600-1674e8508ee9d6%22%2C%22%24device_id%22%3A%221674e8508edd7-06c7f3cb02379c-4313362-2073600-1674e8508ee9d6%22%7D; sajssdk_2015_cross_new_user=1; _putrc=C9F82ECF865F5394123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B79791; hasDeliver=0; gate_login_token=9c93a6dfaec17eaab477fc2ed246cf13b9fab656b8df15afeb2471e1646a80d6; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543210663; LGRID=20181126133747-67f55365-f13d-11e8-8bfc-5254005c3644"
        }
    }

    rules = (
        # Rule(LinkExtractor(allow=('zhaopin/.*',)), follow=True),
        Rule(LinkExtractor(allow=('gongsi/\d+.html',)), follow=True),
        # Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def parse_job(self, response):
        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()

        return job_item

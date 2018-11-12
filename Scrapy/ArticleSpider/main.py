# -*- coding:utf-8 -*-
# @Author : "Jlruuu"
# @Time : 2018/8/27 9:52

from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'jobbole'])
# execute(['scrapy', 'crawl', 'jobbole'])
execute(['scrapy', 'crawl', 'lagou'])

# -*- coding:utf-8 -*-
# @Author : "Jlruuu"
# @Time : 2018/11/10 16:05
import hashlib

def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

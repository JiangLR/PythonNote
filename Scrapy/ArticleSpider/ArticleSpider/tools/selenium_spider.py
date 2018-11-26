# -*- coding:utf-8 -*-
# @Author : "Jlruuu"
# @Time : 2018/11/25 14:46

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='G:\\selenuim\\chromedriver.exe')

browser.get("https://www.oschina.net/blog")

time.sleep(5)

for i in range(3):
    browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    time.sleep(3)

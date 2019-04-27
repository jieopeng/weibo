# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn',"weibo.com"]
    start_urls = ['https://m.weibo.cn/api/container/getIndex?sudaref=login.sina.com.cn&display=0&retcode=6102&type=uid&value=2803301701&containerid=1076032803301701']


    def start_requests(self):
        url = self.start_urls[0]
        yield Request(url)
    def parse(self, response):
          datas = json.loads(response.text)
          # json_data = json.(datas).encode('utf-8').decode('unicode_escape')
          f = open("json.html","w",encoding="utf-8")
          f.write(str(datas))
          print(datas)




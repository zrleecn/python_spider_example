# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']


    def start_requests(self):
        print("登陆")
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "18507584705", "password": "zrlee.cn"},
            callback=self.parse_page

        )

    def parse_page(self, response):
        with open("zrlee_renren.html", "wb+") as filename:
            filename.write(response.body)



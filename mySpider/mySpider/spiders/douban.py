# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    url = "https://movie.douban.com/top250?start="
    start = 0
    start_urls = [url + str(start)]

    def parse(self, response):
        for each in response.xpath("//div[@class='info']"):
            item = DoubanspiderItem()
            item['name'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            item['score'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            yield item

        if self.start < 225:
            self.start += 25
            yield scrapy.Request(self.url + str(self.start), callback=self.parse)




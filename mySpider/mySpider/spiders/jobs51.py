# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import Job51spiderItem


class Jobs51Spider(CrawlSpider):
    """
        51job.com 招聘网爬虫类
    """
    name = 'jobs51'
    allowed_domains = ['51job.com']
    start_urls = ['https://jobs.51job.com/guangzhou-byq/jisuanjiruanjian/p1/']

    content_link = LinkExtractor(allow=r'/jisuanjiruanjian/p\d+')
    rules = (
        Rule(content_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 岗位 //div[@class='e ']/p[@class='info']/span[@class='title']/a/@title
        # 公司 //div[@class='e ']/p[@class='info']/a/@title
        # 地点 //div[@class='e ']/p[@class='info']/span[@class='location name']/text()
        # 薪水 //div[@class='e ']/p[@class='info']/span[@class='location']/text()

        print(response.url)
        for each in response.xpath("//div[@class='e ']"):
            # 实例化对象
            item = Job51spiderItem()
            # 岗位
            name = each.xpath("./p[@class='info']/span[@class='title']/a/@title").extract()[0]
            # 公司名称
            company = each.xpath("./p[@class='info']/a/@title").extract()[0]
            # 地点
            location = each.xpath("./p[@class='info']/span[@class='location name']/text()").extract()[0]
            # 薪水
            salary = each.xpath("./p[@class='info']/span[@class='location']/text()").extract()[0]
            item['name'] = name
            item['company'] = company
            item['location'] = location
            item['salary'] = salary
            # 数据交给pipelines 处理数据
            yield item























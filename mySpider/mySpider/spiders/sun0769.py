# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import Sun0769spiderItem
import re


class Sun0769Spider(CrawlSpider):
    """
        阳光问政爬虫雷
    """
    name = 'sun0769'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=2&page=1']

    page_link = LinkExtractor(allow=r'type=2&page=\d+')
    # page_link1 = LinkExtractor(allow=r'type=2&page=')
    content_link = LinkExtractor(allow=r'/html/question/\d+/\d+\.shtml', deny_domains=r'/error/404\.htm')
    rules = (
        Rule(page_link, process_links="deal_link" ),
        Rule(content_link, callback="parse_item", follow=True, process_links="deal_link"),

    )

    def parse_item(self, response):
        # pass
        print(response.url)
        item = Sun0769spiderItem()
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        yield item


    def deal_link(self, links):

        # 这个网站会反爬虫 返回假的链接 http://www.sun0769.com/error/404.htm
        pattern = re.compile(r'error/404')
        for each in links:
            # print(each.url)
            # 去掉假的链接
            print(each.url)

            if pattern.search(each.url):
                print(each.url)
                links.remove(each)

        return links

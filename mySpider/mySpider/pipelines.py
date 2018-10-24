# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.conf import settings
import pymongo


class Job51spiderPipeline(object):

    def __init__(self):
        self.filename = open("job51.json", "wb")

    def process_item(self, item, spider):
        text = (json.dumps(dict(item), ensure_ascii=False) + ",\n").encode("utf-8")
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()


class Sun0769spiderPipeline(object):

    def __init__(self):
        self.filename = open("sun0769.json", "wb")

    def process_item(self, item, spider):
        text = (json.dumps(dict(item), ensure_ascii=False) + ",\n").encode("utf-8")
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()



class DoubanspiderItem(object):
    """
    豆瓣电影爬虫
    """
    def __init__(self):
        # 服务器读取配置项
        host = settings.get('MONGODB_HOST')
        port = settings.get('MONGODB_PORT')
        dbname = settings.get('MONGODB_DBNAME')

        # 客户端连接
        client = pymongo.MongoClient(host=host, port=port)

        # 选择数据库
        db = client[dbname]
        # 选择表
        self.table = db[settings.get('MONGODB_DOCNAME')]

    def process_item(self, item, spider):
        # 保存到mongodb
        self.table.insert(dict(item))




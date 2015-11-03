# -*- coding: utf-8 -*-

from scrapy import signals
import json
import codecs
import pymongo
from scrapy.conf import settings

class HuxiuPipeline(object):


#mongodb

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'huxiu-20151029')

        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item



#json

    # def __init__(self):
    #     self.file = codecs.open('huxiu.json',  'w', encoding='utf-8')
    #
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    #
    # def spider_closed(self, spider):
    #     self.file.close()

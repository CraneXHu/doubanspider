# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class DoubanspiderPipeline(object):

    def __init__(self):
#        self.file = open('E:\Project\doubanspider\doubanspider\items.txt', 'w')
        self.names_seen = set()
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
#        line = json.dumps(dict(item)) + "\n"
#        self.file.write(line)
        if item['name'] in self.names_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.names_seen.add(item['name'])
            self.collection.insert(dict(item))
            return item

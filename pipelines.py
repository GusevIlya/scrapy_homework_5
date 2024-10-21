# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class LabirintBooksPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.labirint_books

    def process_item(self, item, spider):
        item['_id'] = item.get('_id').split('/')[-2]
        item['autor'] = item.get('autor').split(': ')[0]
        item['title'] = item.get('title').split(': ')[1]
        try:
            item['price'] = int(item.get('price'))
        except:
            item['price'] = 'not defined'
        try:
            item['year'] = int(item.get('year')[1].lstrip(', ').rstrip(' г.'))
        except:
            item['year'] = 'not defined'

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

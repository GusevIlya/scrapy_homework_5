# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LabirintBooksItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    autor = scrapy.Field()
    title = scrapy.Field()
    publisher = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UnicodescraperItem(scrapy.Item):
    encoded = scrapy.Field()
    name = scrapy.Field()
    numeric = scrapy.Field()

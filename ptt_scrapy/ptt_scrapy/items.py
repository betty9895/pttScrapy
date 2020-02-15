# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttScrapyItem(scrapy.Item):

    title = scrapy.Field()
    herf = scrapy.Field()
    # date = scrapy.Field()
    # author = scrapy.Field()

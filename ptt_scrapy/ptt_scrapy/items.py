# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttScrapyItem(scrapy.Item):
    href = scrapy.Field()
    title = scrapy.Field()
    time=scrapy.Field()
    author=scrapy.Field()
    url=scrapy.Field()

    positive=scrapy.Field()
    negative=scrapy.Field()
    score=scrapy.Field()
    comment_num=scrapy.Field()

    img=scrapy.Field()
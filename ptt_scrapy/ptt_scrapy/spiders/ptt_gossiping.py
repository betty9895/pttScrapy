# -*- coding: utf-8 -*-
import scrapy
from ..items import PttScrapyItem


class PttGossipingSpider(scrapy.Spider):
    name = 'ptt_gossiping'
    allowed_domains = ['ptt.cc']


    def start_requests(self):
        yield scrapy.Request("https://www.ptt.cc/bbs/Gossiping/index39709.html",cookies={'over18':'1'})

    def parse(self, response):
        for sel in response.css("div.r-ent"):
            item = PttScrapyItem()
            item["title"] = response.css("div.title").extract()
            item["herf"] = response.css("div.title>a").extract()
            # item["date"] = response.css("").extract()
            # item["author"] = response.css("").extract()
            yield item

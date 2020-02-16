# -*- coding: utf-8 -*-
import scrapy
from ..items import PttScrapyItem


class PttGossipingSpider(scrapy.Spider):
    name = 'ptt_gossiping'
    allowed_domains = ['ptt.cc']

    def __init__(self):
        self.num_of_pages = 0
        self.max_pages = 50
        

    def start_requests(self):
        yield scrapy.Request("https://www.ptt.cc/bbs/Gossiping/search?q=%E6%96%B0%E8%81%9E", cookies={'over18': '1'})

    def parse(self, response):
        # for sel in response.css("div.r-ent"):
        #     item = PttScrapyItem()
        #     item["href"] = response.css("div.title a::attr(href)").extract()
        #     yield item

        # 自動點開每篇文章，並將索取的網頁傳至parae_post()擷取所需項目
        for href in response.css("div.title a::attr(href)").extract():
            href = response.urljoin(href)
            yield scrapy.Request(href, callback=self.parse_post)

        # 頁數計算
        self.num_of_pages = self.num_of_pages+1

        # 自動翻頁
        if self.num_of_pages < self.max_pages:
            pre_page = response.xpath("//*[@id='action-bar-container']/div/div[2]/a[2]/@href")
            if pre_page:
                url = response.urljoin(pre_page[0])
                yield scrapy.Request(url, callback=self.parse_post)
            else:
                print("目前頁數:", self.num_of_pages)
        else:
            print("已經到達最大頁數", self.max_pages)

    def parse_post(self, response):
        item = PttScrapyItem()
        # item["href"]
        item["title"] = response.xpath("//*[@id='main-content']/div[3]/span[2]/text()").extract()
        item["time"] = response.xpath("//*[@id='main-content']/div[4]/span[2]/text()").extract()
        item["author"] = response.xpath("//*[@id='main-content']/div[1]/span[2]/text()").extract()
        item["url"] = response.css("#main-content > a::attr(href)").extract()
        
        comment_num=0
        positive=0
        negative=0
        comments=response.xpath("//div[@class='push']")
        for comment in comments:
            comment_num+=1
            push=comment.css("span.hl.push-tag::text")[0].extract()
            if "推" in push:
                positive+=1
            elif "噓" in push:
                negative+=1

        score=positive-negative
        # item["push_author"]=response.xpath()
        # item["push_content"]=response.xpath()
        # item["push_ip"]=response.xpath()
        item['positive']=positive
        item['negative']=negative
        item['score']=score
        item['comment_num']=comment_num
        yield item

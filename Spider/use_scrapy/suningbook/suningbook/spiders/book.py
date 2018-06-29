# -*- coding: utf-8 -*-
import scrapy
import re


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['snbook.suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")
        for li in li_list:
            a_list = li.xpath("./div[@class='three-sort']/a")
            for a in a_list:
                item = {}
                item['type'] = a.xpath("./text()").extract_first()
                item['type_url'] = a.xpath("./@href").extract_first()
                item['type_url'] = "http://snbook.suning.com" + item['type_url']
                yield scrapy.Request(
                    item['type_url'],
                    callback=self.parse_type,
                    meta={'item': item}
                )

    def parse_type(self, response):
        item = response.meta['item']
        print(response.request.url,"*"*50)
        li_list = response.xpath("//ul[@class='clearfix']/li")
        for li in li_list:
            item['book_url'] = li.xpath("./div[@class='book-img']/a/@href").extract_first()
            yield scrapy.Request(
                item['book_url'],
                callback=self.parse_detail,
                meta={'item': item}
            )

        current_page = response.xpath("//a[@class='current']/text()")
        next_url = response.xpath("//a[@class='next']").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                item['type_url']+'pageNumber={}&sort=0'.format(int(current_page)+1),
                callback=self.parse_type()
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['book_img'] = response.xpath("//dl[@class='brief-img fl']/dt/img/@src").extract_first()
        item['book_name'] = response.xpath("//div[@class='brief-info fl']/h1/strong/text()").extract_first()
        item['book_author'] = response.xpath("//div[@class='parm parm-author wauto']/a/text()").extract_first()
        item['book_price'] = re.findall("\"bp\":'(.*?)',", response.body.decode())[0]
        item['book_content'] = response.xpath("//div[@class='i-brief clearfix']//p[1]/text()").extract_first()
        yield item




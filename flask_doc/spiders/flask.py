# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from flask_doc.items import PageItem


class FlaskSpider(CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']

    rules = (
            Rule(LinkExtractor(allow='http://flask.pocoo.org/docs/0.12/.*'),
            callback='parse_page',
            follow=True),
    )

    def parse_page(self, response):
        item = PageItem()
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
        """
        todo 补充url和text的解析规则
        """
        item['url'] = response.url
        item['text'] = ' '.join(response.xpath('//text()').extract())
#        text_h1 = response.xpath('//div[@class="body"]/div[@class="section"]/h1/text()').extract()

#       text_h1_p = response.xpath('//div[@class="body"]/div[@class="section"]/p/text()').extract()

#        text_h2_p = response.xpath('//div[@class="body"]/div[@class="section"]/div[@class="section"]/p/text()').extract()
#        text_h2 = response.xpath(' //div[@class="body"]/div[@class="section"]/div[@class="section"]/h2/text()').extract()
        
#        item['text'] = text_h1+text_h1_p+text_h2+text_h2_p
        
        yield item

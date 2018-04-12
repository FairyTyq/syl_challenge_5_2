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
        Rule(LinkExtractor(allow=r'',restrict_xpaths=('//a[@class="reference internal"]')),
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
        item['url']=str(response.url).encode('utf-8')
        item['text']=response.xpath('//div[@class="body"]/div[@class="section"]/div[@class="section"]/p/text()').extract_first()
        yield item

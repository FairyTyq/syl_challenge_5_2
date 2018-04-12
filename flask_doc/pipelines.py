# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        """
        todo:将item结果以JSON形式保存到Redis数据库的list结构中
        """
        self.open_spider(spider)
        tmp_data = json.dumps({'url':str(item['url']),'text':item['text']})
        self.redis.lpush("flask_doc",tmp_data)
        print(tmp_data)

        return item

    def open_spider(self,spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)

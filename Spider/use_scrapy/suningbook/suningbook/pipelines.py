# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SuningbookPipeline(object):
    def process_item(self, item, spider):
        with open('suning_book.txt', 'a') as f:
            f.write(json.dumps(item, ensure_ascii=False, indent=2))

        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EduaidscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    awardName = scrapy.Field()
    description = scrapy.Field()
    #restrictions
    host = scrapy.Field()



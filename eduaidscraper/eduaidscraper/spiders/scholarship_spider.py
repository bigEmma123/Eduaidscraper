# -*- coding: utf-8 -*-
import scrapy
from ..items import EduaidscraperItem


class ScholarshipSpiderSpider(scrapy.Spider):
    name = 'scholarship'
    allowed_domains = ['https://www.internationalscholarships.com']
    start_urls = ['https://www.internationalscholarships.com/scholarships']

    def parse(self, response):
        items = EduaidscraperItem()

        awardName = response.css(
            'tr+ tr td:nth-child(1) a , #award-grid a+ a').css('::text').extract()
        description = response.css(
            'tr:nth-child(14) td:nth-child(1) , td:nth-child(2) , tr:nth-child(13) a').css('::text').extract()

        host = response.css(
            '.award-restriction:nth-child(2)').css('::text').extract()
        

        items['awardName'] = awardName
        items['description'] = description
        items['host'] = host
        

        yield items




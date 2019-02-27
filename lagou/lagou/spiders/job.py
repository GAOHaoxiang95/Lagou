# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
	PAGES = 10
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']
	base_url = 'https://www.lagou.com/zhaopin/C++/'
	_url = 'https://www.lagou.com/zhaopin/C++/4/'
	json = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=1'
    def start_requests(self):
        for i in range(PAGES):
			url = base_url + str(i) + '/'
			yield Request(url=url, callback=self.parse)
	def parse(self, response):
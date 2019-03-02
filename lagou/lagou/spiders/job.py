# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import FormRequest
from scrapy import Request
import json
import time
import copy
from lagou.items import LagouItem

class JobSpider(scrapy.Spider):
	name = 'job'
	PAGES = 3
	allowed_domains = ['lagou.com']
	base_url = 'https://www.lagou.com/jobs/positionAjax.json?'
	url = 'https://www.lagou.com/jobs/list_.net?'
	form_data = []
	def start_requests(self):
		base_data = {'first':'true', 'pn':'1', 'kd' : '.net'}
		for i in range(self.PAGES):
			data = copy.deepcopy(base_data)
			data['pn'] = str(i+1)
			self.form_data.append(data)
		print(self.form_data)
		self.form_data = iter(self.form_data)
		
		for i in range(self.PAGES):
			yield Request(url = self.url, callback=self.parse,dont_filter = True)
			time.sleep(8)

	def parse(self, response):		
		form_data = next(self.form_data)
			
		yield FormRequest(url=self.base_url, formdata = form_data, callback=self.parse_item)
		time.sleep(8)
			
	def parse_item(self, response):
		r = json.loads(response.text)
		item = LagouItem()
		try:
			for i in r.get('content').get('positionResult').get('result'):
				item['name'] = i.get('companyFullName')
				item['ctype'] = i.get('firstType')
		except e:
			print(e)
			
		

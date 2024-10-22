import scrapy
import csv
from test import response


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]
# divannewparss = []

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name' : divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }



# -*- coding: utf-8 -*-
import scrapy
import urlparse
from UnicodeScraper.items import *

class FileformatSpider(scrapy.Spider):
    name = "fileformat"
    allowed_domains = ["www.fileformat.info"]
    start_urls = (
        'http://www.fileformat.info/info/charset/UTF-8/list.htm',
    )

    def parse(self, response):
        for line in response.xpath('//tr[re:test(@class, "row[01]$")]'):
            content = line.xpath("td//text()").extract()
            if content[0] == "More...":
                print line
                lnk = urlparse.urljoin(response.url, line.xpath(".//a/@href").extract()[0])
                yield scrapy.Request(lnk)
            else:
                if len(content) == 3:
                    item = UnicodescraperItem(encoded = content[0], name = content[1], numeric = content[2])
                    yield item



import scrapy

class zipperspider(scrapy.Spider):
    name = "zipperspider"
    start_urls = ["http://192.168.206.180/zipper/"]
    def parse(self, response):
        for every_line in response.css('img'):
            yield {
                'Image Link is': every_line.xpath('@src').extract_first(),
            }
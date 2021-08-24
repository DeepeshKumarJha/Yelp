import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ['yelp.com', ]

    def start_requests(self):
        yield scrapy.Request(
            url=self.link,
            callback=self.parse
        )

    def parse(self, response):
        pass

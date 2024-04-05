import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import Homework6Item
from itemloaders.processors import MapCompose



class UnsplashSpider(CrawlSpider):
    name = "unsplash"
    allowed_domains = ["www.unsplash.com"]
    start_urls = ["https://www.unsplash.com"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//div[@class='zmDAx']/a")), callback="parse_item", follow=True),)

    def parse_item(self, response):
        loader = ItemLoader(item=Homework6Item(), response=response)

        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath('name', '//h1/text()')

        loader.add_xpath('category', '//span/a[@class="IQzj8 eziW_"]/text()')

        loader.add_xpath('image_urls', '//div[@class="btXSB"]/div/div/button/div/div/img/@scrset')
        
        yield loader.load_item()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Homework6Item(scrapy.Item):
    name = scrapy.Field() 
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

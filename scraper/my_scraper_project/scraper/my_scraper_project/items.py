import scrapy

class MyScraperProjectItem(scrapy.Item):
    # Jo data save karna hai uske fields define karein
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
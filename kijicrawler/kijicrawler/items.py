# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    phone=scrapy.Field()
    address=scrapy.Field()
    dateposted=scrapy.Field()
    def __str__(self):
        return str(self['name']) + str(self['phone']) + str(self['address']) + str(self['dateposted'])

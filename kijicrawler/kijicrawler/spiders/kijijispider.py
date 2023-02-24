from scrapy import Spider
from scrapy.selector import Selector
from kijicrawler.items import LeadItem
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime
import re
class KSpider(Spider):
    pass 


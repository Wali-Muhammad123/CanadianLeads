from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime
import re
from scrapy.http import FormRequest
from utils import hiddenvaluescraper
from exceptions import *
class KSpider(Spider):
    username="jimpeterson68.89@gmail.com"
    password="Sam12345@"
    name="kspider"
    login_url="https://id.kijiji.ca/login"
    def start_requests(self):
        return scrapy.Request(login_url,callback=self.login)
    def login(self,response):
        try:
            execution=hiddenvaluescraper(response,'execution')
            service=hiddenvaluescraper(response,'service')
            state=hiddenvaluescraper(response,'state')
            nonce=hiddenvaluescraper(response,'nonce')
            locale=hiddenvaluescraper(response,'locale')
            kc_locale=hiddenvaluescraper(response,'kc_locale')
            scope=hiddenvaluescraper(response,'scope')
            tmSessionId=hiddenvaluescraper(response,'tmSessionId')
            _eventId=hiddenvaluescraper(response,'_eventId')
            geolocation=hiddenvaluescraper(response,'geolocation')
            return FormRequest.from_response(response,formdata={
                'execution':execution,
                'service':service,
                'state':state,
                'nonce':nonce,
                'locale':locale,
                'kc_locale':kc_locale,
                'scope':scope,
                'tmSessionId':tmSessionId,
                '_eventId':_eventId,
                'geolocation':geolocation,
                'username':username,
                'password':password
            },callback=self.start_scraping)
        except:
            raise UserNotAllowedException(message="User not allowed to login")
    def start_scraping(self,response):
        print("This is the response",response)



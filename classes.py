import requests
names_list=['James','Jonathan']
area_codes=[]
class ZyteScraper:
    API_KEY=''
    BASE_URL=''
    def __init__(self,names_list, area_codes):
        self.names=names_list
        self.codes=area_codes
    def sendrequest(self,name,area_code):
        self.api_response=requests.post(
            'https://api.zyte.com/v1/extract',
            auth=(API_KEY,''),
            json={
                'url':BASE_URL+name+area_code, #Recreate the url so that it can send GET requests accordingly
                'browserHtml': True,
            },
        )
        return self.api_response
    def crawl(self,name_list,area_code_list):
        pass
    def scraper(self):
        pass


# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Fetcher:
    def __init__(self,url):
        self.url =url
        

    def lookup(self):
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        link = self.url.replace(" ", "+")
        source=requests.get(link, headers=headers).text
        soup=BeautifulSoup(source,"html.parser")
        answer =soup.find('div',class_="Z0LcW").get_text()
        return answer
        
            

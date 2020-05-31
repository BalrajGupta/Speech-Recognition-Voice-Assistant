# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime
import webbrowser

class Fetcher:
    def __init__(self):
        self.url=""

    def lookup(self,url):
        self.url=url
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        link = self.url.replace(" ", "+")
        source=requests.get(link, headers=headers).text
        soup=BeautifulSoup(source,"html.parser")
        try:
            answer =soup.find('div',class_="Z0LcW").get_text()
        except:
            answer= "Sorry, I can't help you with that yet."
        return answer
        

        


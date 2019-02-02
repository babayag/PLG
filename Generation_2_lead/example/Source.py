import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Source():
    def __init__(self):
        self.sources = []


    def search(self, li_number, lipath):
        apath = lipath[li_number].findNext("h2").find("a", href=True)
        source = apath["href"]
        return source


    def appendSource(self, source):
       if type(source) != type('git example'):
           emppty = 'Not'
           return emppty
       else:
           self.sources.append(source)
           return self.sources

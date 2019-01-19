import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Source():
    def __init__(self):
        self.sources = []

    def search(self, li_number, driver):
        sources = ''
        apath = driver.find_elements_by_xpath('//h2/a')[li_number]
        source = apath.get_attribute("href")
        #print(li_number)
        #apath = self.driver.find_elements_by_xpath('//h2/a')[self.li_number]
        #emailSource = apath.get_attribute("href")
        #self.sources.append(self.emailSource)
        #print(len(self.sources))
        #return self.emailSource
        #print( self.emailSource)
        return source


    def appendSource(self, source):
        self.sources.append(source)
        return self.sources

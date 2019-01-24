import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Source():
    def __init__(self):
        self.sources = []

    def search(self, li_number, driver):
        apath = driver.find_elements_by_xpath('//h2/a')[li_number]
        source = apath.get_attribute("href")

        return source


    def appendSource(self, source):
        self.sources.append(source)
        return self.sources

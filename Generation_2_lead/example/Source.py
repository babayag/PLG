import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class Source():
    def __init__(self, driver, li_number):
        self.driver = driver
        self.li_number = li_number
        self.sources = []

    def search(self):
        apath = self.driver.find_elements_by_xpath('//h2/a')[self.li_number]
        emailSource = apath.get_attribute("href")
        self.sources.append(emailSource)
        print(len(self.sources))
        return emailSource


    def appendSource(self, a):
        self.sources.append(a)

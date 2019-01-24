import re

from numpy.testing import _private
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class BingSearch():

    def search(self, enterUrl):
        pageNumber = 1
        url = "https://www.bing.com/search?q=%40{}&first={}".format(enterUrl, pageNumber)#put the url of the site into the object url of type str
        options = Options()
        options.headless = True # define the option of chrome webdriver,Returns whether or not the headless argument is set
        driver = webdriver.Chrome(options=options)
        driver.get(url) # get the url, return an object of type NoneType
        return driver


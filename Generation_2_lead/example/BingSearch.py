import re

from numpy.testing import _private
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class BingSearch():


    def __init__(self, enterUrl):
        self.pageNumber = 1
        self.enterUrl = enterUrl
        self.options = Options()# initialise the object options with the options of chrome webdriver, return the object options of type selenium.webdriver.chrome.options.Options
        self.driver = webdriver.Chrome(options = self.options, executable_path = r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\chrome driver\chromedriver.exe')
        # create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver

    def search(self):
        url = "https://www.bing.com/search?q=%40{}&first={}".format(self.enterUrl,self.pageNumber)#put the url of the site into the object url of type str
        self.options.headless = True # define the option of chrome webdriver,Returns whether or not the headless argument is set
        self.driver.get(url) # get the url, return an object of type NoneType
        return self.driver

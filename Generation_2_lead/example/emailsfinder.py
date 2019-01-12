#-------------------------------------------------------------------------------
# Name:        Email Scraper
# Purpose:      Create a that find email address by the domain name
#
# Author:      Beny-DZIENGUE
#
# Created:     03/01/2019
# Copyright:   (c) Beny-DZIENGUE 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import needed object
import re
import sys

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class EmailFinderService():
    # initialise the object emails, which will contains the emails founds

  def getEmail(enterUrl):

        emails = []
        emailSources = []
        AllData = []
        #get the url, return an object of type str


        #enter = input("Enter the url without 'www' : ")
        # initialise the object pageNumber to 1, return an object of type int
        pageNumber = 1


        #put the url of the site into the object url of type str
        url = "https://www.bing.com/search?q=%40{}&first={}".format(enterUrl,pageNumber)
        #initialise the object options with the options of chrome webdriver, return the object options of type selenium.webdriver.chrome.options.Options
        options = Options()
        #define the option of chrome webdriver,Returns whether or not the headless argument is set
        options.headless = True
        #create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver
        driver = webdriver.Chrome(options=options, executable_path=r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\chrome driver\chromedriver.exe')
        #get the url, return an object of type NoneType
        driver.get(url)


        pageNumber = 2
        #condition to run the program in infinity
        while  True :

            li_number = 0
            while True:
                try:
                    lipath = driver.find_elements_by_class_name("b_algo")[li_number]
                    litext = lipath.text
                    #for line in the drivertextclear
                    for line in litext.splitlines():
                        #search all email in each line, return the objet searchNumbers of type list
                        searchEmails = re.findall(r"\w*[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl),line, flags=re.MULTILINE)
                            #for email in email_1 list

                        if searchEmails:
                            apath = driver.find_elements_by_xpath('//h2/a')[li_number]
                            emailSource = apath.get_attribute("href")
                            for email in searchEmails:
                                    # if email not in the emails list
                                if email not in emails:
                                        # add email in the emails list: return an object oy type NoneType
                                    emails.append(email)
                                    emailSources.append(emailSource)
                                    print(email)

                    li_number =li_number + 1

                except:
                    break
            try:
                # look for the html tag that content a specific str number : return the object link of type str
                link = driver.find_element_by_link_text(str(pageNumber))
                #number.append(str(pageNumber))
            # if an error occur
            except :
                #stop the while loop
                break
            #click of the link that is in the tag found in link : return an object of type NoneType
            link.click()
            #add 1 to the page number to have the number of the next pageL: return the object page_number of type int
            pageNumber += 1

        for i in range(len(emails)):
            FinalJson = {"email":emails[i], "url":emailSources[i]}
            AllData.append(FinalJson)
        return AllData


        driver.quit()
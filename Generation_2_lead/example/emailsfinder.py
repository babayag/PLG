
#import needed object
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class EmailFinderService():
    # initialise the object emails, which will contains the emails founds



    def checking(self, email, url):
        options = Options()
        # define the option of chrome webdriver,Returns whether or not the headless argument is set
        options.headless = True
        # create a webdriver object, return the object driver of type selenium.webdriver.chrome.webdriver.WebDriver
        driver = webdriver.Chrome(options=options,  executable_path=r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\chrome driver\chromedriver.exe')

        driver.get(url)

        # select the bar search
        barSearch = driver.find_element_by_name("email")
        # write the email address in the bar search
        barSearch.send_keys(email)

        # select the submit button
        button = driver.find_element_by_class_name("Button")
        # click the button
        button.click()

        # create a beautifulsoup object, return an object of type bs4.BeautifulSoup
        soup = BeautifulSoup(driver.page_source, features="html.parser")

        result = soup.select("td")
        success = result[-1].text
        if success == "E-mail address is valid":
            return True
        else:
            return False


    def getEmail(self,enterUrl):

        emails = []
        emailSources = []
        AllData = []

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
                                emails.append(email)
                                emailSources.append(emailSource)
                                    # if email not in the emails list
                    li_number =li_number + 1

                except:
                    break
            try:
                # look for the html tag that content a specific str number : return the object link of type str
                link = driver.find_element_by_link_text(str(pageNumber))
            # if an error occur
            except :
                #stop the while loop
                break
            #click of the link that is in the tag found in link : return an object of type NoneType
            link.click()
            #add 1 to the page number to have the number of the next pageL: return the object page_number of type int
            pageNumber += 1


        for email, source in zip(emails, emailSources):
            AllData.append("{} {}".format(email, source))

        emails = []
        emailSources = []
        newEmails = []
        newEmailSources = []
        newCheck = []
        output = sorted(AllData)

        data = []
        for items in output:
            emails.append(items.split(" ")[0])
            emailSources.append(items.split(" ")[1])

        # put the url of the site into the object url of type str
        url = "http://mailtester.com/testmail.php"

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in newEmails:
                checks = self.checking(self, mail, url)
                if checks == True:
                    newCheck.append(True)
                else:
                    newCheck.append(False)
                newEmails.append(mail)
                newEmailSources.append(emailSources[index:index + count])
                index += count

        #print(emails)
        #print(emailSources)

        for emailsCounter in range(len(newEmails)):
            jsonReturn = {
                "email": newEmails[emailsCounter],
                "isValide": newCheck[emailsCounter],
                "url": newEmailSources[emailsCounter]
            }
            data.append(jsonReturn)

        return data

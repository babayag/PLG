
#import needed object
import re
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import http.client
import socket
from bs4 import BeautifulSoup

class EmailFinderService():
    # initialise the object emails, which will contains the emails founds

<<<<<<< HEAD


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

=======
    def get_page(page):
        try:
            # always set a timeout when you connect to an external server
            url = "www.bing.com"
            connection = http.client.HTTPSConnection(url, timeout=10)

            connection.request("GET", page)

            response = connection.getresponse()

            return response.read()
        except socket.timeout:
            # in a real world scenario you would probably do stuff if the
            # socket goes into timeout
            pass

    def nbrPage(self, enterUrl):
        page = "/search?q=%40{}&first=11".format(enterUrl)
        result = self.get_page(page)
        soup = BeautifulSoup(result, features="html.parser")
        txt = soup.find("span", {"class": "sb_count"}).text
        txt = txt.split(" ")[-2]
        liste = []
        for nbr in range(1, int(txt), 10):
            liste.append("/search?q=%40{}&first={}".format(enterUrl, nbr))
            dif = int(txt) - nbr
            if dif <= 10:
                liste.append("/search?q=%40{}&first={}".format(enterUrl, nbr + dif))
        return liste
>>>>>>> 7b595ce12aed41b99c9a1bacaf2ec05dd5b8dadb

    def getEmail(self,enterUrl):


        emails = []
        emailSources = []
        emailSource = []
        AllData = []
        urls = self.nbrPage(self, enterUrl)


<<<<<<< HEAD
        driver = webdriver.Chrome(options=options, executable_path=r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\chrome driver\chromedriver.exe')
        #get the url, return an object of type NoneType
        driver.get(url)

        pageNumber = 2
=======
>>>>>>> 7b595ce12aed41b99c9a1bacaf2ec05dd5b8dadb
        #condition to run the program in infinity
        with PoolExecutor(max_workers=7) as executor:
            for _ in executor.map(self.get_page, urls):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0
                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list
                            searchEmails = re.findall(r"\w*[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl), line,flags=re.MULTILINE)
                            # for email in email_1 list
                            if searchEmails:
                                apath = lipath[li_number].findNext("h2").find("a", href=True)
                                emailSource = apath["href"]
                                for email in searchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    emails.append(email)
                                    emailSources.append(emailSource)
                        li_number = li_number + 1
                    except:
                        break

        print(emails)
        #print(emailSource)

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

                newEmails.append(mail)
                newEmailSources.append(emailSources[index:index + count])
                index += count

        #print(emails)
        print(emailSources)

        for emailsCounter in range(len(newEmails)):
            jsonReturn = {
                "email": newEmails[emailsCounter],
                "url": newEmailSources[emailsCounter]
            }
            data.append(jsonReturn)

        return data

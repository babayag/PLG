

import re
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from bs4 import BeautifulSoup
from .BingSearch import BingSearch
from .Source import Source
from .JsonStructure import JsonStructure
from .FileManager import FileManager

class Email():

    def __init__(self):
        self.emails = []
        self.sources = []
        self.AllData = []

    def returnTenEmails(self, p, fileContent):
        result = []
        allEmails = fileContent[0:len(fileContent)-2]
        #print("eusebio")
        #print(len(allEmails))
        p = int(p)
        if len(allEmails[p:]) >= 10:
            emailsToReturn = allEmails[p:(p+10)]
            result.append(emailsToReturn)
            p += len(emailsToReturn)
            #print("eusebio2")
            #print(len(emailsToReturn))
            result.append(p)
            result.append(True)
            return result
        else:
            emailsToReturn = allEmails[p:]
            #print('eusebio3')
            #print(len(emailsToReturn))
            result.append(emailsToReturn)
            p += len(emailsToReturn)
            result.append(p)
            result.append(True)
            return result

    def DownloadEmails(self, enterUrl):
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            # URL is valid
            pureUrl = BingSearch.extractGoodDomain(BingSearch, enterUrl)
            FileManager.__init__(FileManager)
            if FileManager.verifyIfFileExist(FileManager,pureUrl) == True:
                # File exist in the directory
                FileManager.__init__(FileManager)
                fc = FileManager.readFile(FileManager, pureUrl)
                emailsToReturn = fc[0:len(fc)-2]
                return emailsToReturn
            else:
                return " FILE IS NOT EXIST !!!"
        else:
            return 'YOU ENTERED A BAD URL !!!'

    def main(self, enterUrl, p):
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            # URL is valid
            pureUrl = BingSearch.extractGoodDomain(BingSearch, enterUrl)
            FileManager.__init__(FileManager)
            if FileManager.verifyIfFileExist(FileManager, pureUrl) == True:
                # File exist in the directory
                print("File exist in the directory")
                FileManager.__init__(FileManager)
                fc = FileManager.readFile(FileManager, pureUrl)
                nbrPage = FileManager.GetLastPageNumber(FileManager, pureUrl)
                emailsToReturn = self.returnTenEmails(self, p, fc)
                if len(emailsToReturn[0]) == 10:
                    return emailsToReturn
                else:
                    if fc[2] == False:
                        #impossible to find new emails on bing
                        #print("impossible to find new emails on bing 1")
                        emailsToReturn[2] = False # remove the button see more of the view
                        print(1)
                        return emailsToReturn
                    else:
                        #possible to find new emails on bing
                        #print("possible to find new emails on bing 2")
                        urls = BingSearch.nbrPage(BingSearch, pureUrl, nbrPage)
                        scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                        if scrapedEmail == False:
                            # file has been not updated
                            #print("file has been not updated")
                            print(2)
                            emailsToReturn[2] = False # remove the button see more of the view
                            return  emailsToReturn
                        else:
                            # file has been updated
                            #print('file has been updated')
                            print(3)
                            FileManager.__init__(FileManager)
                            fc = FileManager.readFile(FileManager, pureUrl)
                            emailsToReturn = self.returnTenEmails(self, p, fc)
                            return emailsToReturn
            else: 
                # File is not exist
                #print("File is not exist")
                
                urls = BingSearch.nbrPage(BingSearch, pureUrl, None)
                scrapedEmail = Email.getEmail(Email, urls,pureUrl)
                if scrapedEmail == True:
                    print(4)
                    FileManager.__init__(FileManager)
                    fc = FileManager.readFile(FileManager, pureUrl)
                    emailsToReturn = self.returnTenEmails(self, p, fc)
                    return emailsToReturn
                else:
                    print(5)
                    return []
        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!! please entered a url like itkamer.com'

    def getEmail(self, urls,pureUrl):
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            for _ in executor.map(BingSearch.initialSearch, urls[0]):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0

                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list

                            searchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(pureUrl), line,flags=re.MULTILINE)
                            # for email in email_1 list

                            if searchEmails:
                                src = Source.search(Source, li_number, lipath)
                                for email in searchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    self.emails.append(email)
                                    self.sources = Source.appendSource(Source, src)
                        li_number = li_number + 1
                    except:
                        break

        datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, self.emails, self.sources, pureUrl, urls[1])

        return datasStructured

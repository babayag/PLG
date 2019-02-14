

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
        if fileContent[0][p:] >= 10:
            emails = fileContent[0][p:(p+10)]
            result[0] = emails
            p+= len(emails['email'])
            result[1] = p
            result[2] = False
            return result
        else:
            emails = fileContent[0][p:]
            result[0] = emails
            p += len(emails['email'])
            result[1] = p
            result[2] = False
            return result



    def main(self, enterUrl, p):
        if BingSearch.UrlValidation(BingSearch,enterUrl) == True:
            # URL is valid
            FileManager.__init__(FileManager)
            if FileManager.verifyIfFileExist(FileManager, enterUrl):
                # File exist in the directory
                fc = FileManager.readFile(FileManager, enterUrl)
                nbrPage = fc[1]
                emailsToReturn = self.returnTenEmails(self, p, fc)
                if len(emailsToReturn[0]) == 10:
                    return emailsToReturn
                else:
                    if !fc[2]:
                        emailsToReturn[2] = False
                        return emailsToReturn
                    else:
                        urls = BingSearch.nbrPage(BingSearch, enterUrl, lastPageNumber)
                        scrapedEmail = 
            
            else: 
                # File is not exist

        else:
            # URL is not valid
            return 'YOU ENTERED A BAD URL!! please entered a url like itkamer.com'

    def getEmail(self, urls,enterUrl):
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

                            searchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl), line,flags=re.MULTILINE)
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

        datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, self.emails, self.sources, enterUrl, urls[1])

        return datasStructured
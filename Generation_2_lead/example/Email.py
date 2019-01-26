

import re
from .BingSearch import BingSearch
from .Source import Source

from .JsonStructure import JsonStructure

class Email():

    def __init__(self):
        #self.driver = driver
        self.emails = []
        self.sources = []
        self.AllData = []


    def getEmail(self,enterUrl):
        driver = BingSearch.search(BingSearch, enterUrl)
        pageNumber = 2
        Source.__init__(Source)
        while True:
            li_number = 0
            while True:
                try:
                    lipath = driver.find_elements_by_class_name("b_algo")[li_number]
                    litext = lipath.text

                    # for line in the drivertextclear
                    for line in litext.splitlines():
                        # search all email in each line, return the objet searchNumbers of type list
                        searchEmails = re.findall(r"\w*[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl), line, flags=re.MULTILINE)
                        print(searchEmails)

                        if searchEmails:
                            source = Source.search(Source, li_number, driver)
                            for email in searchEmails:
                                self.emails.append(email)
                                self.sources = Source.appendSource(Source, source)
                                #print(self.emails)
                    li_number = li_number + 1
                except:
                    break
            try:
                # look for the html tag that content a specific str number : return the object link of type str
                link = driver.find_element_by_link_text(str(pageNumber))
            # if an error occur
            except:
                # stop the while loop
                break
            # click of the link that is in the tag found in link : return an object of type NoneType
            link.click()
            # add 1 to the page number to have the number of the next pageL: return the object page_number of type int
            #print(self.emails)
            #print(self.sources)
            pageNumber += 1

        JsonStructure.__init__(self)
        c = JsonStructure.JsonStructureReturn(JsonStructure, self.emails, self.sources)
        return c
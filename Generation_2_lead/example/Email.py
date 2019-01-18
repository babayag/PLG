

import re
from .Source import Source

class EmailFinderService():

    def __init__(self, driver):
        self.driver = driver
        self.pageNumber = 1
        self.li_number = 0
        self.emails = []


    def getEmail(self,enterUrl):

        while True:
            while True:
                try:
                    lipath = self.driver.find_elements_by_class_name("b_algo")[self.li_number]
                    litext = lipath.text

                    # for line in the drivertextclear
                    for line in litext.splitlines():
                        # search all email in each line, return the objet searchNumbers of type list
                        searchEmails = re.findall(r"\w*[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl), line, flags=re.MULTILINE)

                        if searchEmails:
                            Source.__init__(Source, self.driver, self.li_number)
                            source = Source.search(Source)
                            for email in searchEmails:
                                self.emails.append(email)
                                Source.appendSource(source)
                                print(self.emails)
                               # emailSources.append(emailSource)
                                # if email not in the emails list


                    self.li_number = self.li_number + 1

                except:
                    break
            try:
                # look for the html tag that content a specific str number : return the object link of type str
                link = self.driver.find_element_by_link_text(str(self.pageNumber))
            # if an error occur
            except:
                # stop the while loop
                break
            # click of the link that is in the tag found in link : return an object of type NoneType
            link.click()
            # add 1 to the page number to have the number of the next pageL: return the object page_number of type int

            self.pageNumber += 1


        return Source.sources
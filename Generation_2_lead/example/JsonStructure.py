import re
import os
import json
from bs4 import BeautifulSoup
from django.utils.decorators import method_decorator

class JsonStructure():
    def JsonStructureReturn(self, Nemails, Nsources, enterUrl):
        emails = []
        allData = []
        data = []
        emailSources = []
        newEmails = []
        newEmailSources = []
        for email, source in zip(Nemails, Nsources):
            allData.append("{} {}".format(email, source))

        output = sorted(allData)

        for items in output:
            emails.append(items.split(" ")[0])
            emailSources.append(items.split(" ")[1])

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in newEmails:
                newEmails.append(mail)
                
                sourceWithoutDbl = []
                for counter in emailSources[index:index + count]:
                    if counter not in sourceWithoutDbl: sourceWithoutDbl.append(counter)
                newEmailSources.append(sourceWithoutDbl)
                index += count

        for emailsCounter in range(len(newEmails)):
            jsonReturn = {
                "email": newEmails[emailsCounter],
                "url": newEmailSources[emailsCounter]
            }
            print(jsonReturn)
            data.append(jsonReturn)
        os.chdir(r'C:\Users\euseb\Desktop\DEV\Projet Django\PLG\Generation_2_lead\example\Nouveau dossier')
        try:
            with open("{}.json".format(enterUrl), 'w') as outfile:
                json.dump(data, outfile)
        except FileNotFoundError:
            pass
        return data


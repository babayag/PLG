from .FileManager import FileManager


class JsonStructure():
    def getFiveFirstEmail(self, fc, data):
        print(fc)
        result = 0
        newData = []
        allEmails = fc[0:len(fc) - 2]
        index = None
        idx = []
        if len(allEmails) >= 5:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(allEmails)):
                    if data[idOfNewDatas]['email'] == allEmails[idOfEmail]['email']:
                        if index not in idx:
                            idx.append(index)
                        if data[idOfNewDatas]['url'][0] in allEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'][
                            0] == allEmails[idOfEmail]['url']:

                            result = result + 1
                            newData.append(data[idOfNewDatas])
                        else:
                            allEmails[idOfEmail]['url'].append(data[idOfNewDatas]['url'])
           
          
            if result == len(data):
                return result
            else:
                return 0

        else:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(allEmails)):
                    if data[idOfNewDatas]['email'] == allEmails[idOfEmail]['email']:
                        #   elm = data.pop(index)
                        if data[idOfNewDatas]['url'] in allEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'] == \
                                allEmails[idOfEmail]['url']:
                            result = result + 1
            if result == len(data):
                return result
            else:
                return 0
        
        """lengthOfData1 = len(data)
        for i in idx:
            print("cas 112")
            lengthOfData2 = len(data)
            if lengthOfData1 == lengthOfData2:
                
                del data[1]
                print("cas 1")
                print(len(data))
            else:
                for y in range(len(idx)):
                    idx[y] = idx[y] - 1
                del data[i]
                print("cas 2")
                print(len(data))"""
    
    def JsonStructureReturn(self, Nemails, Nsources, enterUrl, LastpageNbr):

        self.LastpageNbr = LastpageNbr
        emails = []
        data = []
        emailSources = []
        allData = []

        newEmails = []
        newEmailSources = []
        for email, source in zip(Nemails, Nsources):
            allData.append("{} {}".format(email, source))

        #trie par ordre alphabetique
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
            data.append(jsonReturn)

        FileManager.__init__(FileManager)
        counter = 0
        if FileManager.verifyIfFileExist(FileManager, enterUrl):
            fc = FileManager.readFile(FileManager, enterUrl)
            counter = self.getFiveFirstEmail(self, fc, data)
        dataReturn = False
        if counter != 0:
            FileManager.__init__(FileManager)
            # FileManager.updateCanSearch(FileManager, enterUrl)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, False)
            dataReturn = False
        else:
            FileManager.__init__(FileManager)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, True)
            dataReturn = True

        return dataReturn


    def StructureMultipleDomains(self,Nemails, Nsources, goodUrl):

        emails = []
        allData = []
        data = []
        emailSources = []
        newEmails = []
        newEmailSources = []
        datafinal = []

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
                    if counter not in sourceWithoutDbl:
                        sourceWithoutDbl.append(counter)
                newEmailSources.append(sourceWithoutDbl)
                index += count

        # we initialise DomainEmailAndUrl with content Domain and list of email and url
        DomainEmailAndUrl = {
            "Domain": goodUrl,

            "concern": []
        }

        # for emails index in range len(newEmails)
        
        DomainEmailAndUrl = {}
        for emailsCounter in range(len(newEmails)):

            EmailAndUrl ={
                "email": newEmails[emailsCounter],
                "url": newEmailSources[emailsCounter]
            }
            #append email and Url in the data list
            data.append(EmailAndUrl)

            DomainEmailAndUrl = {
                "Domain": goodUrl,
                # set data list content to concern attribut
                "concern": data
            }

        return DomainEmailAndUrl

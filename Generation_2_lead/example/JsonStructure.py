from .FileManager import FileManager


class JsonStructure():
    def getFiveFirstEmail(self, fc, data):
        result = 0
        newData = []
        allEmails = fc[0:len(fc) - 2]
        index = None
        idx = []
        if len(allEmails) >= 5:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(allEmails)):
                    print('yes')
                    print(data[idOfNewDatas]['email'])
                    print(allEmails[idOfEmail]['email'])
                    if data[idOfNewDatas]['email'] == allEmails[idOfEmail]['email']:
                        if index not in idx:
                            idx.append(index)
                        if data[idOfNewDatas]['url'][0] in allEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'][
                            0] == allEmails[idOfEmail]['url']:

                            result = result + 1
                            newData.append(data[idOfNewDatas])
                            print(result)
                        else:
                            allEmails[idOfEmail]['url'].append(data[idOfNewDatas]['url'])
            print("eusebio")
            print(result)
            print("length of data")
            print(data)
            print("7777777777777777")
            print(newData)
            if result == len(data):
                return result
            else:
                return 0

        else:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(allEmails)):
                    print('yes')
                    print(data[idOfNewDatas]['email'])
                    print(allEmails[idOfEmail]['email'])
                    if data[idOfNewDatas]['email'] == allEmails[idOfEmail]['email']:
                        #   elm = data.pop(index)
                        if data[idOfNewDatas]['url'] in allEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'] == \
                                allEmails[idOfEmail]['url']:
                            result = result + 1
            if result == len(data):
                return result
            else:
                return 0

    def JsonStructureReturn(self, Nemails, Nsources, enterUrl, LastpageNbr):
        self.LastpageNbr = LastpageNbr
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
            data.append(jsonReturn)

        FileManager.__init__(FileManager)
        counter = 0
        if FileManager.verifyIfFileExist(FileManager, enterUrl):
            fc = FileManager.readFile(FileManager, enterUrl)
            counter = self.getFiveFirstEmail(self, fc, data)
        print(counter)
        dataReturn = False
        if counter != 0:
            print("to update")
            FileManager.__init__(FileManager)
            # FileManager.updateCanSearch(FileManager, enterUrl)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, False)
            dataReturn = False
        else:
            print("no update")
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
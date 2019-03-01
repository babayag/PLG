

from .FileManager import FileManager

class JsonStructure():
    def getFiveFirstEmail(self,fc,data):
        result = 0
        allEmails = fc[0:len(fc)-2]
        
        if len(allEmails) >= 5:
            print("==============")
            print(len(data))
            print("==============")
            for newDatas in data:
                index = 0
                for email in allEmails:
                    if newDatas['email'] == email['email']:
                        if newDatas['url'] != email['url']:
                            # url are #
                            for myUrl in newDatas['url']:
                                email['url'].append(myUrl)
                                result = result + 1
                            index = data.index(newDatas)
                            del data[index]
                        else:
                            # URL are same
                            if newDatas['url'][0] == email['url'][0]:
                                result = result + 1
                            index = data.index(newDatas)
                            del data[index]
                    #del data[index]
            print("==========")
            print("Value of result")
            print(result)
            print("==========")

            if result != 0:
                return result
            else:
                return 0
        else:
            for newDatas in data:
                for email in allEmails:
                    if newDatas['email'] == email['email']:
                        if newDatas['url'] == email['url']:
                            result = result + 1
                    print(result)
            print(len(data))
            if result != 0:
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

            jsonReturn ={
                    "email": newEmails[emailsCounter],
                    "url": newEmailSources[emailsCounter]
                }
            data.append(jsonReturn)
            #print("Tshutsho")
            #print(data)
        #pagination
        #fiveFirstEmailOfData = data[slice(0,5,1)]
        FileManager.__init__(FileManager)
        counter = 0
        if FileManager.verifyIfFileExist(FileManager, enterUrl):
            fc = FileManager.readFile(FileManager,enterUrl)
            counter = self.getFiveFirstEmail(self,fc,data)
        #fiveFirstEmailOfFile = FileManager.getFiveFirstEmail(FileManager, enterUrl)
        
        dataReturn = False
        print("eusebio")
        print(counter)
        if counter != 0:
            print("to update")
            FileManager.__init__(FileManager)
            #FileManager.updateCanSearch(FileManager, enterUrl)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, False)
            dataReturn = False
        else:
            print("no update")
            FileManager.__init__(FileManager)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, True)
            dataReturn = True

        return dataReturn

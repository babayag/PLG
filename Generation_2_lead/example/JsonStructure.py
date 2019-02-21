

from .FileManager import FileManager

class JsonStructure():
    def getFiveFirstEmail(self,fc,data):
        result = 0
        allEmails = fc[0:len(fc)-2]
        
        if len(allEmails) >= 5:
            for newDatas in data:
                for email in allEmails[0:5]:
                    if newDatas['email'] == email['email']:
                        print(newDatas['url'])
                        print(email['url'])
                        if newDatas['url'] == email['url']:
                            result = result + 1
                    print(result)
            print("==========")
            print(len(data))
            print("==========")
            if result == len(data):
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
        '''if result == 5:
            return result
        else:
            result = 0
            return result'''
    
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

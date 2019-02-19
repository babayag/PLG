from .FileManager import FileManager

class JsonStructure():
    def getFiveFirstEmail(self, fc, data):
        result = 0
        allEmails = fc[0:len(fc)-2] 
        if len(allEmails) >= 5:
            if len(data) >= 5:
                for newDatas in data:
                    if newDatas in allEmails:
                        result = result + 1
                    else:
                        result = 0
                print('len(data) >= 5')
                print(result)
                return result
            else:
                for newDatas in  data:
                    if newDatas in allEmails:
                        result = result + 1
                        print(result)
                print('else of len(data) >= 5')
                print(result)
                return result
        else:
            # if len(allEmails) >= len(data):
            for newDatas in data:
                if newDatas in allEmails:
                    result = result + 1
                else:
                    result = 0
            print('len(allEmails) >= len(data)')
            print(result)
            return result
            # else:
            #     for newDatas in data:
            #         if newDatas in allEmails:
            #             result = result + 1
            #         else:
            #             result = 0
            #     print('elese of len(allEmails) >= len(data)')
            #     print(result)
            #     return result

    def JsonStructureReturn(self, Nemails, Nsources, enterUrl, LastpageNbr):
        self.LastpageNbr = LastpageNbr
        emails = []
        allData = []
        data = []
        emailSources = []
        newEmails = []
        newEmailSources = []
        # print(Nemails) 
        # print(Nsources)
        for email, source in zip(Nemails, Nsources):
            allData.append("{} {}".format(email, source))
        # print(allData)

        output = sorted(allData)

        for items in output:
            emails.append(items.split(" ")[0])
            emailSources.append(items.split(" ")[1])

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in newEmails:
                newEmails.append(mail)
                print(newEmails)
                
                sourceWithoutDbl = []
                for counter in emailSources[index:index + count]:
                    if counter not in sourceWithoutDbl:
                       sourceWithoutDbl.append(counter)
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
            counter = self.getFiveFirstEmail(self, fc, data)
        #fiveFirstEmailOfFile = FileManager.getFiveFirstEmail(FileManager, enterUrl)
        
        dataReturn = False
        """if len(fiveFirstEmailOfFile) != 0:
            counter = 0
            for  x_values, y_values in zip(fiveFirstEmailOfFile, fiveFirstEmailOfData):
                if sorted(x_values['email']) == sorted(y_values['email']):
                    counter = counter + 1
                    #print(counter)
                else:
                    counter = 0"""
        #print(counter)
        if counter != 0:
            print("to update")
            FileManager.__init__(FileManager)
            #FileManager.updateCanSearch(FileManager, enterUrl)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, False)
            dataReturn = False
            """if counter == len(fiveFirstEmailOfFile):
                FileManager.__init__(FileManager)
                FileManager.updateCanSearch(FileManager, enterUrl)
                dataReturn = False
                #print(" == 5")
            else:
                if counter == 100:
                    FileManager.__init__(FileManager)
                    FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, True)
                    dataReturn = True
                    #print("== 100")
                else:
                    FileManager.__init__(FileManager)
                    FileManager.updateCanSearch(FileManager, enterUrl)
                    dataReturn = False
                    #print("# de 0")"""
        else:
            FileManager.__init__(FileManager)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, True)
            dataReturn = True
        return dataReturn

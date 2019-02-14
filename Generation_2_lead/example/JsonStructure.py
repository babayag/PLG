

from .FileManager import FileManager

class JsonStructure():

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
        #pagination
        fiveFirstEmailOfData = data[slice(0,5,1)]
        FileManager.__init__(FileManager)
        fiveFirstEmailOfFile = FileManager.getFiveFirstEmail(FileManager, enterUrl)
        counter = 100
        dataReturn = False
        if len(fiveFirstEmailOfFile) != 0:
            counter = 0
            for  x_values, y_values in zip(fiveFirstEmailOfFile, fiveFirstEmailOfData):
                print(x_values)
                if sorted(x_values['email']) == sorted(y_values['email']):
                    counter = counter + 1
                    #print(counter)
                else:
                    counter = 0
        print(counter)
        if counter != 0:

            if counter == len(fiveFirstEmailOfFile):
                FileManager.__init__(FileManager)
                FileManager.WriteInFile(FileManager, None, enterUrl, None, False)
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
                    FileManager.WriteInFile(FileManager, None, enterUrl, None, False)
                    dataReturn = False
                    #print("# de 0")
        else:
            FileManager.__init__(FileManager)
            FileManager.WriteInFile(FileManager, data, enterUrl, self.LastpageNbr, True)
            dataReturn = True

        return dataReturn

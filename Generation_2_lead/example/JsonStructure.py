from .FileManager import FileManager


class JsonStructure():

    """
    author : Essongo Joel Stephane
    params : fc, data
    description : ?????????????????
    return : ask to Essongo
    """
    def GetFiveFirstEmail(self, fc, data):
        result = 0
        NewData = []
        AllEmails = fc[0:len(fc) - 2]
        index = None
        idx = []
        if len(AllEmails) >= 5:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(AllEmails)):
                    if data[idOfNewDatas]['email'] == AllEmails[idOfEmail]['email']:
                        if index not in idx:
                            idx.append(index)
                        if data[idOfNewDatas]['url'][0] in AllEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'][
                            0] == AllEmails[idOfEmail]['url']:

                            result = result + 1
                            NewData.append(data[idOfNewDatas])
                        else:
                            AllEmails[idOfEmail]['url'].append(data[idOfNewDatas]['url'])
           
          
            if result == len(data):
                return result
            else:
                return 0

        else:
            for idOfNewDatas in range(len(data)):
                # index = data.index(newDatas)
                for idOfEmail in range(len(AllEmails)):
                    if data[idOfNewDatas]['email'] == AllEmails[idOfEmail]['email']:
                        #   elm = data.pop(index)
                        if data[idOfNewDatas]['url'] in AllEmails[idOfEmail]['url'] or data[idOfNewDatas]['url'] == \
                                AllEmails[idOfEmail]['url']:
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
    
    
    """
    author : ?????????????????????
    params : Nemails,Nsources,Enterurl,LastpageNbr
    description : tranform a data to a json form
    return : filecontent with boolean which tell if already exist or no
    """
    def JsonStructureReturn(self, Nemails, Nsources, EnterUrl, LastpageNbr):
        self.LastpageNbr = LastpageNbr
        emails = []
        AllData = []
        data = []
        EmailSources = []
        NewEmails = []
        NewEmailSources = []
        for email, source in zip(Nemails, Nsources):
            AllData.append("{} {}".format(email, source))

        output = sorted(AllData)


        for items in output:
            emails.append(items.split(" ")[0])
            EmailSources.append(items.split(" ")[1])

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in NewEmails:
                NewEmails.append(mail)

                sourceWithoutDbl = []
                for counter in EmailSources[index:index + count]:
                    if counter not in sourceWithoutDbl: sourceWithoutDbl.append(counter)
                NewEmailSources.append(sourceWithoutDbl)
                index += count

        for emailsCounter in range(len(NewEmails)):
            jsonReturn = {
                "email": NewEmails[emailsCounter],
                "url": NewEmailSources[emailsCounter]
            }
            data.append(jsonReturn)

        FileManager.__init__(FileManager)
        counter = 0
        if FileManager.VerifyIfFileExist(FileManager, EnterUrl):
            fc = FileManager.ReadFile(FileManager, EnterUrl)
            counter = self.GetFiveFirstEmail(self, fc, data)
        dataReturn = False
        if counter != 0:
            FileManager.__init__(FileManager)
            # FileManager.updateCanSearch(FileManager, EnterUrl)
            FileManager.WriteInFile(FileManager, data, EnterUrl, self.LastpageNbr, False)
            dataReturn = False
        else:
            FileManager.__init__(FileManager)
            FileManager.WriteInFile(FileManager, data, EnterUrl, self.LastpageNbr, True)
            dataReturn = True

        return dataReturn


    """
    author : Ranyl Foumbi
    params : Nemails, Nsources, goodUrl
    description : structure result for bulk search before send it to frontend app
    return:DomainEmail And Url

    """
    def StructureMultipleDomains(self,Nemails, Nsources, goodUrl):

        emails = []
        AllData = []
        data = []
        EmailSources = []
        NewEmails = []
        NewEmailSources = []
        Datafinal = []

        for email, source in zip(Nemails, Nsources):
            AllData.append("{} {}".format(email, source))

        output = sorted(AllData)

        for items in output:
            emails.append(items.split(" ")[0])
            EmailSources.append(items.split(" ")[1])

        index = 0
        for mail in emails:
            count = emails.count(mail)
            if mail not in NewEmails:
                NewEmails.append(mail)

                sourceWithoutDbl = []
                for counter in EmailSources[index:index + count]:
                    if counter not in sourceWithoutDbl:
                        sourceWithoutDbl.append(counter)
                NewEmailSources.append(sourceWithoutDbl)
                index += count

        # we initialise DomainEmailAndUrl with content Domain and list of email and url
        DomainEmailAndUrl = {
            "Domain": goodUrl,

            "concern": []
        }

        # for emails index in range len(NewEmails)
        
        DomainEmailAndUrl = {}
        for emailsCounter in range(len(NewEmails)):

            EmailAndUrl ={
                "email": NewEmails[emailsCounter],
                "url": NewEmailSources[emailsCounter]
            }
            #append email and Url in the data list
            data.append(EmailAndUrl)

            DomainEmailAndUrl = {
                "Domain": goodUrl,
                # set data list content to concern attribut
                "concern": data
            }

        return DomainEmailAndUrl

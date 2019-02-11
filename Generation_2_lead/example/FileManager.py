import os
import json
from datetime import datetime
import time

class FileManager():

    def WriteInFile(self,data,enterUrl,LastpageNbr):

        os.chdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache')
        if self.verifyIfFileExist(self,enterUrl):
            fdata = []
            try:
                with open("{}.json".format(enterUrl), 'r') as outfile:
                    fdata = json.load(outfile)
                    del fdata[-1]

                with open("{}.json".format(enterUrl), 'w') as outfile:
                    fdata.append(data)
                    fdata.append({"LastpageNbr": LastpageNbr})
                    json.dump(fdata, outfile)
            except FileNotFoundError:
                pass

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    json.dump(data, outfile)

            except FileNotFoundError:
                pass


    def GetLastPageNumber(self, enterUrl):

        os.chdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache')
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-1]['LastpageNbr']
        except FileNotFoundError:
            return None
        return lastNumber



    def verifyIfFileExist(self,enterUrl):
        FileManager.storeDomain(FileManager,enterUrl)
        os.chdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache')
        try:
            if os.path.isfile("{}.json".format(enterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass

    def getFiveFirstEmail(self,enterUrl):
        fiveFirstEmail =[]
        os.chdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache')
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                fiveFirstEmail = fdata[slice(0,5,1)]

        except FileNotFoundError:
            pass

        return fiveFirstEmail


    def clearDirectory(self,timeOfLifeOfFile):

        timeOfEachFile = []
        currentTime = time.mktime(datetime.now().timetuple())

        #for each file in the folder
        for file in os.listdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache'):

            timeOfCreation = os.path.getmtime(file)  # get file creation/modification time

            #if the currentTime - time of file creation is grather than 30 days delete the file
            if currentTime - timeOfCreation > timeOfLifeOfFile:
                os.remove(file)  # delete outdated file
            else:
                timeOfEachFile.append(timeOfCreation)  # add time info to list
    # after check all files, choose the oldest file creation time from list
        _sleep_time = (currentTime - min(
            timeOfEachFile)) if timeOfEachFile else 120  # if _time_list is empty, set sleep time as 120 seconds, else calculate it based on the oldest file creation time
        time.sleep(_sleep_time)


    def storeDomain(self,enterUrl):
        domainName = []
        # for each file in the folder"
        cacheFolderPath = os.listdir(r'E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\cache')
        domainFile = "E:\SEMESTRE III\programmation projet\LeadmeHome\PLG\Generation_2_lead\example\DomainsName\Domain.txt"
        for file in cacheFolderPath:

            if file not in domainFile:
                domainName.append(file)
                return 'Not in domainFile'
        url = (enterUrl + ".json")
        if url not in domainName:
            domainName.append(url)
            return 'Not in domainName'
        with open(domainFile, 'w') as outfile:
            outfile.write("[")
            for item in domainName:
                outfile.write("'"+ item +"'"+","+ "\n")
            outfile.write("]")
            return 'file is up to date'

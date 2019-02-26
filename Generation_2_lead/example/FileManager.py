import os
import json
from datetime import datetime
import time

class FileManager():

    def __init__(self):
        self.cacheFolderPath = r'E:\paness IIHT\M2\project\Nouveau dossier\PLG\Generation_2_lead\example\cache'
        self.domainFile = r"E:\paness IIHT\M2\project\Nouveau dossier\PLG\Generation_2_lead\example\DomainsName\Domain.txt"

    def WriteInFile(self, data, enterUrl, LastpageNbr, canSearch):
        os.chdir(self.cacheFolderPath)
        if self.verifyIfFileExist(self,enterUrl):
            fdata = []
            try:
                with open("{}.json".format(enterUrl), 'r') as outfile:
                    fdata = json.load(outfile)
                    #delete the two last element of the list which are LastpageNbr and canSearch
                    del fdata[-1]
                    del fdata[-1]

                with open("{}.json".format(enterUrl), 'w') as outfile:
                    for item in data:
                        if item not in fdata:
                           fdata.append(item)
                    fdata.append({"LastpageNbr": LastpageNbr})
                    fdata.append({"canSearch": canSearch})
                    json.dump(fdata, outfile)
            except FileNotFoundError:
                pass
            return True

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    data.append({"canSearch": canSearch})
                    json.dump(data, outfile)

            except FileNotFoundError:
                pass
            return False


    def GetLastPageNumber(self, enterUrl):

        os.chdir(self.cacheFolderPath)
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-2]['LastpageNbr']
        except FileNotFoundError:
            return None
        return lastNumber



    def verifyIfFileExist(self,enterUrl):
        os.chdir(self.cacheFolderPath)
        try:
            if os.path.isfile("{}.json".format(enterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass

    def readFile(self, enterUrl):
        #open the folder and return its contents
        os.chdir(self.cacheFolderPath)
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                fileContent = json.load(printer)
                return fileContent
        except FileNotFoundError:
            pass

    """def getFiveFirstEmail(self,fc,data):
        result = 0
        allEmails = fc[0:len(fc)-2]
        if len(allEmails) >= 5:
            for x_values, y_values in zip(allEmails[0:5], data[0:5]):
                if sorted(x_values['email']) == sorted(y_values['email']):
                    result = result + 1
                    return result
                else:
                    result = 0
                    return result
        else:
            for x_values, y_values in zip(allEmails[0:1], data[0:1]):
                if sorted(x_values['email']) == sorted(y_values['email']):
                    result = result + 1
                    return result
                else:
                    result = 0
                    return result


        fiveFirstEmail =[]
        os.chdir(self.cacheFolderPath)
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                fiveFirstEmail = fdata[slice(0, 5, 1)]

        except FileNotFoundError:
            pass

        return fiveFirstEmail'''"""


    def clearDirectory(self,timeOfLifeOfFile):

        timeOfEachFile = []
        currentTime = time.mktime(datetime.now().timetuple())

        #for each file in the folder
        for file in os.listdir(self.cacheFolderPath):

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


    def updateCanSearch(self,enterUrl):
        os.chdir(self.cacheFolderPath)
        fdata = []
        try:
            with open("{}.json".format(enterUrl), 'r') as outfile:
                fdata = json.load(outfile)
                del fdata[-1]
                #print(fdata)
            with open("{}.json".format(enterUrl), 'w') as outfile:
                fdata.append({"canSearch": False})
                json.dump(fdata, outfile)
        except FileNotFoundError:
            pass

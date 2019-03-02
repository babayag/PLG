#import needed object
import requests
import objectpath
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import datetime
import re
#import itertools
import sys

class GenerateValidEmail():

    def printInvalidEntry(self,name,patternFirstnameAndLastname):
        #print a message and stop the program if the name is not matching the pattern or is empty
        if patternFirstnameAndLastname.search(name)or name == "":
            pass
        else:
            #sys.exit("Invalid {0}".format([ k for k,v in locals().iteritems() if v == name][0]))
            print("Sorry, but the firstname or the lastname is invalid")
            sys.exit()
        return 0

    def verifyEntry(self,firstname,lastname,domainName):
    #method which verify is what the user enter match with the firstname, lastname or domain parttern
        #set firstname and lastname pattern : return the object patternFirstnameAndLastname of type _sre.SRE_Pattern
        patternFirstnameAndLastname = re.compile("^[\w\_\-\.\ ]+$")
        # set domain pattern : return the object patternDomain of type _sre.SRE_Pattern
        patternDomain = re.compile("^\w+\.\w+$")
        #verify if firstname is valid        
        self.printInvalidEntry(self,firstname,patternFirstnameAndLastname)
        #verify if lastname is valid 
        self.printInvalidEntry(self,lastname,patternFirstnameAndLastname)

        #print a message and stop the program if the domain is not matching the pattern or is empty
        if patternDomain.search(domainName):
            pass
        else:
            print("Sorry , but you enter an invalid Domain")
            sys.exit()
        return 0
        
    def generatePossibleMailWithTwoEntry(self,firstname,lastname,domainName,listOfEmails):
    #generate all the possible email with two name and keep them in listOfEmails : return an object of type int
        email1 =  firstname[0]+lastname+"@"+domainName
        listOfEmails.append(email1)
        email2 =  firstname+"."+lastname+"@"+domainName
        listOfEmails.append(email2)
        email3 =  lastname+"@"+domainName
        listOfEmails.append(email3)
        email4 =  firstname+"_"+lastname+"@"+domainName
        listOfEmails.append(email4)
        email5 =  firstname[0]+"_"+lastname+"@"+domainName
        listOfEmails.append(email5)
        email6 =  firstname+lastname[0]+"@"+domainName
        listOfEmails.append(email6)
        email7 = firstname+"@"+domainName
        listOfEmails.append(email7)
        email8 = firstname[0]+"@"+domainName
        listOfEmails.append(email8)
        email9 = lastname[0]+"@"+domainName
        listOfEmails.append(email9)
        email10 = firstname[0]+lastname[0]+"@"+domainName
        listOfEmails.append(email10)
        email11 = firstname+lastname+"@"+domainName
        listOfEmails.append(email11)
        email12 = lastname+firstname+"@"+domainName
        listOfEmails.append(email12)
        email13 =  lastname+"."+firstname+"@"+domainName
        listOfEmails.append(email13)
        email14 =  lastname[0]+firstname+"@"+domainName
        listOfEmails.append(email14)
        
    def generatePossibleMailWithOneEntry(self,name,domainName, listOfEmails):
            
        email1 =  name[0]+"@"+domainName
        listOfEmails.append(email1)
        email2 =  name+"@"+domainName
        listOfEmails.append(email2)
        email3 =  "_"+name+"@"+domainName
        listOfEmails.append(email3)

        return listOfEmails

    def generatePossibleMail(self,firstname,lastname,domainName):
        """
        Get first, last name and domain name, and return a list of possible mail
        """
        #initialise the object that will contain all possible name, return the object listOfEmai
        listOfEmails = []
        if len(firstname)> 0 and len(lastname)> 0:
            self.generatePossibleMailWithTwoEntry(self,firstname,lastname,domainName,listOfEmails)
        elif firstname=="" and len(lastname)> 0:
            self.generatePossibleMailWithOneEntry(self,lastname,domainName, listOfEmails)
        elif len(firstname)> 0 and lastname == "":
            self.generatePossibleMailWithOneEntry(self,firstname,domainName, listOfEmails)
        else:
            print("Sorry, but you didn't enter neither a firstname or a lastname")
            sys.exit()
        return listOfEmails

    def verifyEmail(self,email):
        key = '5c7a7118cfeb4'
        requestUrl = "https://api.debounce.io/v1/?api={0}&email={1}&append=false".format(key,email)
        request = requests.post(requestUrl)
        request = request.json()
        jsonTree = objectpath.Tree(request['debounce'])
        resultTuple = tuple(jsonTree.execute('$..result'))
        result = False
        for report in resultTuple:
            if report == 'Safe to Send':
                result = True
            elif report == 'Risky':
                result = True
            else:
                pass
            
        return result

    def returnValidEmail(self,firstname,lastname,domainName):
        
        self.verifyEntry(self,firstname,lastname,domainName)
        validEmails = []
        debut = datetime.datetime.now()
        listOfEmails = self.generatePossibleMail(self,firstname,lastname,domainName)
        with PoolExecutor(max_workers=7) as executor:
                for email in listOfEmails:
                    emails = self.verifyEmail(self,email)
                    if emails == False: 
                        pass
                    else:
                        validEmails.append(email)
                    
        if len(validEmails)> 0 :
            print("Final result : Valid mail")
            for mail in validEmails:
                print(mail)
        else:
            print("Sorry, there's no valid emails for those informations")
        return validEmails

#back end of bus ticket service
#will take Old Central Services File and Merged Transaction Summary File as input
#will output a New Central Services File and New Valid Services File

import sys
import re

mergedTransactionFile = sys.argv[1]
oldCentralFile = sys.argv[2]
newCentralFile = sys.argv[3]
validServiceFile = sys.argv[4]

class Service:
    def __init__(self, number, tickets, name, date):
        self.serviceNumber = number
        self.serviceCapacity = 30
        self.ticketsSold = tickets
        self.serviceName = name
        self.serviceDate = date
        
    #sell tickets function --> adds the number to tickets sold to ticketSold attribute of object
    #throws fatal error if tiketsSold becomes negative or goes above capacity
    #check validity of tickets value and throws an exception if invalid (will always be valid)
    def sellTickets(self, tickets):
        if(tickets > 1000 or tickets < 1):
            raise Exception("Invalid number of tickets")
        self.ticketsSold += tickets
        if(self.ticketsSold > self.serviceCapacity):
            raise Exception("Service over capacity")
        if(self.ticketsSold < 0):
            raise Exception("Number of tickets sold is negative")
    
    #sell tickets function --> removes the number to tickets sold from ticketSold attribute of object
    #throws fatal error if ticketsSold becomes negative or goes above capacity
    #check validity of tickets value and throws an exception if invalid (will always be valid)
    def cancelTickets(self, tickets):
        if(tickets > 1000 or tickets < 1):
            raise Exception("Invalid number of tickets")
        self.ticketsSold -= tickets
        if(self.ticketsSold > self.serviceCapacity):
            raise Exception("Service over capacity")
        if(self.ticketsSold < 0):
            raise Exception("Number of tickets sold is negative")

#uses sellTicket and cancelTicket for remove tickets from one service and add the same number of tickets to another service
def changeTickets(service1, service2, tickets):
    service1.cancelTickets(tickets)
    service2.sellTickets(tickets)

#contains list of serviceNumber, serviceCapacity, ticketsSold, serviceName, serviceDate
def writeNewCS (serviceList):
    centralServices = open(newCentralFile, "w")
    for i in serviceList:
        centralServices.write(serviceList[i].serviceNumber +" "+ serviceList[i].serviceCapacity +" "+ serviceList[i].ticketsSolds +" "+ serviceList[i].serviceName +" "+ serviceList[i].serviceDate)
    centralServices.close()
    
#contains list of all valid service Numbers
def writeNewValid (serviceList):
    validServices = open(validServiceFile, "w")
    for i in serviceList:
        validServices.write(serviceList[i].serviceNumber)
    validServices.close()
    
def deleteService (servicesList, deleteNumber, deleteName):
    listIndex = 0
    for i in servicesList:
        if (i.serviceNumber == deleteNumber) and (i.serviceName == deleteName) and (i.ticketsSold == 0):
            del servicesList[listIndex]
            return servicesList
        #if (i == deleteNumber):
            #del servicesList[listIndex]
        else:
            listIndex += 1
    print ("no matching service number")
    return servicesList

def createService (servicesList, serviceNumber, serviceName, serviceDate):
    #needs class to make
    newService = Service(serviceNumber, 0, serviceName, serviceDate)
    for i in range (0, len(servicesList)):
        if (serviceNumber < servicesList[i].serviceNumber):
            servicesList.insert(i, newService)
            return servicesList
        #if (serviceNumber < servicesList[i]):
            #servicesList.insert(i, serviceNumber)
    servicesList.insert(i+1, newService)
    return servicesList

#central loop   
def main():
    #oldServices = readCentralServices(oldCSFile)
    # transactions = readTransactionFile(mergedTransactionFile)
    
    #adds all old services to the list of services
    serviceList = []
    centralFile = open(oldCentralFile, "r")
    for line in centralFile:
        lineElements = line.split()
        if int(lineElements[1]) < 1000 and int(lineElements[1]) > 0:
            tempObject = Service(lineElements[0], lineElements[2], lineElements[3], lineElements[4])
            serviceList.append(tempObject)
        else:
            raise Exception("Invalid Capacity")
    centralFile.close()
    
    #for x in oldServices:
    #    serviceList.append(Service(oldServices[x][0],oldServices[x][2],oldServices[x][3],oldServices[x][4])
    
    transactions = []
    transactionFile = open(mergedTransactionFile, "r")
    line = transactionFile.readline().rstrip() #get rid of newline
    for line in transactionFile:
        lineElements = line.split()
        transactions.append(lineElements)
    transactionFile.close()
    
    for i in transactions:
        code = i[0]
        number = i[1]
        #exits loop when it reaches the end of the transactions
        if (code == "EOS"):
            break
        #create tickets
        elif (code == "CRE"):
            serviceList = createService(serviceList, transactions[i][0], transactions[i][4], transactions[i][5])
        #delete tickets
        elif (code == "DEL"):
            serviceList = deleteService(serviceList, transactions[i][1], transactions[i][4])
        #sell tickets
        elif (code == "SEL"):
            for y in serviceList:
                if (number == y.serviceNumber):
                    y.sellTickets(i[2])
                else:
                    raise Exception("Service " + number + " doesn't exist")
        #cancel tickets
        elif (code == "CAN"):
             for y in serviceList:
                if (number == y.serviceNumber):
                    y.cancelTickets(i[2])
                else:
                    raise Exception("Service " + number + " doesn't exist")
        #change tickets
        elif (code == "CHG"):
             for y in serviceList:
                if (number == y.serviceNumber):
                    number = i[3]
                    for x in serviceList:
                        if (number == x.serviceNumber):
                            changeTickets(y,x,i[2])
                        else:
                            raise Exception("Service " + number + " doesn't exist")
                else:
                    raise Exception("Service " + number + " doesn't exist")
            
    writeNewCS(serviceList)
    writeNewValid(serviceList)
            
main()

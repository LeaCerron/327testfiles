#back end of bus ticket service
#will take Old Central Services File and Merged Transaction Summary File as input
#will output a New Central Services File and New Valid Services File

import sys
import re

mergedTransactionFile = sys.argv[1]
oldCentralFile = sys.argv[2]
#newCentralFile = sys.argv[3]
#validServiceFile = sys.argv[4]

class Service:
    def __init__(self, number, capacity, tickets, name, date):
        self.serviceNumber = number
        self.serviceCapacity = capacity
        self.ticketsSold = tickets
        self.serviceName = name
        self.serviceDate = date

#contains list of serviceNumber, serviceCapacity, ticketsSold, serviceName, serviceDate
def writeNewCS (serviceList):
    centralServices = open("newCentral.txt", "w")
    for i in serviceList:
        centralServices.write(serviceList[i].serviceNumber +" "+ serviceList[i].serviceCapacity +" "+ serviceList[i].ticketsSolds +" "+ serviceList[i].serviceName +" "+ serviceList[i].serviceDate)
    centralServices.close()
    
#contains list of all valid service Numbers
def writeNewValid (serviceList):
    validServices = open("newValid.txt", "w")
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
    oldServices = readCentralServices(oldCSFile)
    transactions = readTransactionFile(mergedTransactionFile)
    
    #adds all old services to the list of services
    serviceList = []
    for x in oldServices:
        serviceList.append(Service(oldServices[x][0],oldServices[x][1],oldServices[x][2],oldServices[x][3],oldServices[x][4])
    
    for i in transactions:
        code = transactions[i][0]
        number = transactions[i][1]
        for y in serviceList:
            if (number = serviceList[y][0]):
                service1 = y
            else:
                raise Exception("Service " + number + " doesn't exist")
        #exits loop when it reaches the end of the transactions
        if (code = EOS):
            break
        #create tickets
        elif (code = CRE):
            serviceList = createService(serviceList, transactions[i][0], transactions[i][4], transactions[i][5])
        #delete tickets
        elif (code = DEL):
            serviceList = deleteService(serviceList, transactions[i][1], transactions[i][4])
        #sell tickets
        elif (code = SEL):
            serviceList[service1].sellTickets(transactions[i][2])
        #cancel tickets
        elif (code = CAN):
            serviceList[service1].cancelTickets(transactions[i][2])
        #change tickets
        elif (code = CHG):
            number2 = transactions[i][3]
            for x in serviceList:
            if (number2 = serviceList[x][0]):
                service2 = x
            else:
                raise Exception("Service " + number2 + " doesn't exist")
            changeTickets(serviceList[service1], serviceList[service2], transactions[i][2])
            
    writeNewCS(serviceList)
    writeNewValid(serviceList)
            
main()

#back end of bus ticket service
#will take Old Central Services File and Merged Transaction Summary File as input
#will output a New Central Services File and New Valid Services File

import sys

mergedTransactionFile = sys.argv[1]
oldCentralFile = sys.argv[2]
newCentralFile = sys.argv[3]
validServiceFile = sys.argv[4]

class Service:
    def __init__(self, number, tickets, name, date):
        self.serviceNumber = number
        self.serviceCapacity = 30 #since that is default
        self.ticketsSold = tickets
        self.serviceName = name
        self.serviceDate = date
        
    #sell tickets function --> adds the number to tickets sold to ticketSold attribute of object
    #throws fatal error if ticketsSold becomes negative or goes above capacity
    #check validity of tickets value and throws an exception if invalid (will always be valid)
    def sellTickets(self, tickets):
        if(tickets > 1000 or tickets < 1):
            raise Exception("Invalid number of tickets")
        self.ticketsSold += tickets
        if(self.ticketsSold > self.serviceCapacity):
            raise Exception("Service over capacity")
        if(self.ticketsSold < 0):
            raise Exception("Number of tickets sold is negative")
    
    #cancel tickets function --> removes the number to tickets sold from ticketSold attribute of object
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

#writes serviceNumber, serviceCapacity, ticketsSold, serviceName, serviceDate to new central service file
def writeNewCS(serviceList):
    centralServices = open(newCentralFile, "w")
    for i in serviceList:
        centralServices.write(str(i.serviceNumber) + " " + str(i.serviceCapacity) + " " + str(i.ticketsSold) + " " + i.serviceName + " " + str(i.serviceDate) + "\n")
    centralServices.close()
    
#writes new valid service file
def writeNewValid(serviceList):
    validServices = open(validServiceFile, "w")
    for i in serviceList:
        validServices.write(str(i.serviceNumber) + "\n")
    validServices.write("00000") #end of line characters
    validServices.close()
    
#delete service from serviceList when valid
def deleteService(servicesList, deleteNumber, deleteName):
    listIndex = 0
    for i in servicesList:
        if (i.serviceNumber == deleteNumber) and (i.serviceName == deleteName) and (i.ticketsSold == 0):
            del servicesList[listIndex]
            return servicesList
        else:
            listIndex += 1
    print("no matching service number")
    return servicesList

#creates service and add to list if valid
def createService(servicesList, serviceNumber, serviceName, serviceDate):
    #check if new number, return without doing anything if not new
    for i in servicesList:
        if i.serviceNumber == serviceNumber:
            print("service number already exists")
            return servicesList
    newService = Service(serviceNumber, 0, serviceName, serviceDate)
    #insert service to correct place on list
    for i in range(0, len(servicesList)):
        if (serviceNumber < servicesList[i].serviceNumber):
            servicesList.insert(i, newService)
            return servicesList
    servicesList.append(newService)
    return servicesList


#adds all old services to the list of services
def readOldCentralFile():
    serviceList = []
    centralFile = open(oldCentralFile, "r")
    for line in centralFile:
        lineElements = line.split()
        if int(lineElements[1]) < 1000 and int(lineElements[1]) > 0:
            tempObject = Service(int(lineElements[0]), int(lineElements[2]), lineElements[3], int(lineElements[4]))
            serviceList.append(tempObject)
        else:
            raise Exception("Invalid Capacity")
    centralFile.close()
    return serviceList

#make array of each transaction and put them into an array
def readMergedFile():
    transactions = []
    transactionFile = open(mergedTransactionFile, "r")
    #loop through each line in file
    for line in transactionFile:
        lineElements = line.split() #separate elements of transaction into array

        #if service name if string with spaces, still accepts
        while len(lineElements) > 6:
            lineElements[4] = lineElements[4] + " " + lineElements[5]
            del lineElements[5]

        #convert the numeric elements to int
        lineElements[1] = int(lineElements[1])
        lineElements[2] = int(lineElements[2])
        lineElements[3] = int(lineElements[3])
        lineElements[5] = int(lineElements[5])
        transactions.append(lineElements)
    transactionFile.close()
    return transactions
    

#central loop   
def main():
    #create seriveList of service objects
    serviceList = readOldCentralFile()

    #create transaction list
    transactions = readMergedFile()
    
    for i in transactions:
        code = i[0]
        number = int(i[1])
        #exits loop when it reaches the end of the transactions
        if (code == "EOS"):
            break
        #create tickets
        elif (code == "CRE"):
            serviceList = createService(serviceList, i[1], i[4], i[5])
        #delete tickets
        elif (code == "DEL"):
            serviceList = deleteService(serviceList, i[1], i[4])
        #sell tickets
        elif (code == "SEL"):
            x = 0
            for y in serviceList:
                if (number == y.serviceNumber):
                    y.sellTickets(int(i[2]))
                    x += 1
            if(x != 1):
                raise Exception("Service " + str(number) + " doesn't exist")
        #cancel tickets
        elif (code == "CAN"):
            x = 0
            for y in serviceList:
                if (number == y.serviceNumber):
                    y.cancelTickets(i[2])
                    x += 1
            if(x != 1):
                raise Exception("Service " + str(number) + " doesn't exist")
        #change tickets
        elif (code == "CHG"):
            n = 0
            for y in serviceList:
                if (number == y.serviceNumber):
                    number = i[3]
                    n += 1
                    for x in serviceList:
                        if (number == x.serviceNumber):
                            changeTickets(x,y,i[2])
                            n += 1
                            break
                break
            if(n != 2):
                    raise Exception("Service " + str(number) + " doesn't exist")
            
    #when all processed, write output files
    writeNewCS(serviceList)
    writeNewValid(serviceList)
            
main()

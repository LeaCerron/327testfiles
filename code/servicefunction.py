def deleteServices (servicesList, deleteNumber, deleteName):
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

def createServices (servicesList, serviceNumber, serviceName, serviceDate):

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



#newList = [3,5,10,12]
#print (newList)
#deleteServices (newList, 13, "temp")
#createServices (newList, 11, "temp", 1)
#print (newList)


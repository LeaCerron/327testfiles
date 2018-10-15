import datetime

def changeTicket(account, serviceList, changeCounter):
    if (account == "agent") and (changeCounter > 20):
        print("agent cannot change more than 20 in a single session")
        return 0
    
    print("please enter the current service number")
    currentNumber = input()
    if not(currentNumber in serviceList):
        print("invalid service number")
        return 0
    
    print("please enter the new service number")
    newNumber = input()
    if not(newNumber in serviceList):
        print("invalid service number")
        return 0
    
    print("enter the number of tickets you are changing")
    ticketsChanged = input()
    
    if (account == "agent"):
        if ((int(ticketsChanged) + changeCounter) > 20):
            print("agent cannot change more than 20 in a single session")
            return 0
        
    currentDateTime = datetime.datetime.now()
    addToTransactions("CHG " + currentNumber + " " + ticketsChanged + " " +
                     newNumber + " **** " + str(currentDateTime.year) +
                     str(currentDateTime.month) +str(currentDateTime.day) + "\n")
    
    return ticketsChanged
            
        
        


    

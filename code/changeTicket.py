import datetime

def changeTicket(account, serviceList, changeCounter):
    #if the agent has already changed more than 20 tickets, leave immediately
    if (account == "agent") and (changeCounter > 20):
        print("agent cannot change more than 20 in a single session \n")
        return 0
    #gets the current service number    
    currentNumber = input("enter the current service number \n")
    if not(currentNumber in serviceList):
        print("invalid service number")
        return 0
    #gets the new destination service number
    newNumber = input("enter the new service number \n")
    if not(newNumber in serviceList):
        print("invalid service number")
        return 0
    #gets the number of tickets bein changed
    ticketsChanged = input("enter the number of tickets you are changing \n")
    #if agent, checks for the number of tickets changed
    if (account == "agent"):
        if ((int(ticketsChanged) + changeCounter) > 20):
            print("agent cannot change more than 20 in a single session \n")
            return 0
    #checks the current date and adds the trasaction to summary file
    currentDateTime = datetime.datetime.now()
    addToTransactions("CHG " + currentNumber + " " + ticketsChanged + " " +
                     newNumber + " **** " + str(currentDateTime.year) +
                     str(currentDateTime.month) +str(currentDateTime.day) + "\n")
    return int(ticketsChanged) + changeCounter
        
        


    

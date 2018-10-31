#front end of bus ticket service, allows commands over list of services, has user interface
#arguments when running the main are the name of the input file and output file
#will take the valid services file as input
#will output a transaction summary file
import sys

serviceFile = sys.argv[1]
summaryFile = sys.argv[2]

def addToTransactions(transactionCode):
    transaction = open(summaryFile, "a")
    transaction.write(transactionCode)
    transaction.write("\n")
    transaction.close()

#creates a new service based on input from the user; service number, date, and service name
#available only to "planner", returns null if the user inputs any invalid data
def createService(account, serviceList):
    if (account == "agent"):
        print("agent cannot create services")
        return
    #prompts for and validates the service number
    newNumber = input("Enter the new service number: \n")
    if (newNumber in serviceList):
        print("invalid service number")
        return
    elif (newNumber[:1] == "0" or len(newNumber) != 5):
        print("invalid service number")
        return
    #prompts for and validates the service date
    try:
        date = int(input("Enter the date of the service(YYYYMMDD):\n"))
    except:
        print("invalid date")
        return
    if (len(str(date)) > 8):
        print("invalid date\n")
        return
    elif ((date // 10000) > 2999 or (date // 10000) < 1980):
        print("invalid date\n")
        return
    elif ((date % 10000 // 100) > 12 or (date % 10000 // 100) < 1):
        print("invalid date\n")
        return
    elif ((date % 100) > 31 or (date % 100) < 1):
        print("invalid date\n")
        return
    #prompts for and validates the service name
    name = input("Enter a name for the service (3-39 characters, cannot begin/end with a space):\n")
    if (len(name) > 39 or len(name) < 3):
        print("invalid service name")
        return
    elif (name[:1] == " " or name[-1:] == " "):
        print("invalid service name")
        return
    addToTransactions("CRE " + newNumber + " 0 00000 " + name + " " + str(date))
    return

#deletes a pre-existing valid service and prevents any further ticket sales to that service
#available only to "planner"
def deleteService(account, serviceList):
    if (account == "agent"):
        print("agent cannot delete services")
        return
    #checks that the service number is valid
    service = input("Enter the service number to be deleted:\n")
    if not(service in serviceList):
        print("invalid service number")
        return
    #prompts the user for a valid service name
    print("Enter the name of the service to be deleted:")
    name = input()
    if (len(name) > 39 | len(name) < 3):
        print("invalid service name")
        return
    elif (name[0] == " ") or (name[-1] == " "):
        print("invalid service name\n")
        return
    
    addToTransactions("DEL " + service + " 0 00000 " + name + " " + "0")
    return service


def cancelTicket(account, serviceList, cancelCounter, cancelDict):
    serviceNumber = input("Enter a service number: \n")
    if (serviceNumber not in serviceList):
        print("service number not in the valid services list")
        return cancelCounter
    try:
        tickets = int(input("Enter the number ot tickets to cancel: ")) #enter number of tickets
    except:
        print("invalid number of tickets")
        return cancelCounter

    #check number of tickets,must be between 1 and 1000
    if (tickets < 1) | (tickets > 1000):
        print("number of tickets should be between 1 and 1000")
        return cancelCounter
    if (account == 'agent'):
        #agent cannot cancel more than 10 tickets per service per session
        if (tickets + cancelDict[serviceNumber] > 10):
            print("agents are only allowed to delete 10 tickets per service per session")
            return cancelCounter
        if (tickets + cancelCounter > 20):
            #agents cannot cancel more than 20 tickers in one session
            print("agents are only allowed to cancel 20 tickets per session")
            return cancelCounter

    cancelCounter += tickets

    addToTransactions("DEL " + serviceNumber + " " + str(tickets) + " 00000 **** " + "0")
    return cancelCounter


def sellTicket(account, serviceList):
    serviceNumber = input("Enter a service number: \n")
    if (serviceNumber not in serviceList):
        print("Invalid service number")
        return
    #enter number of tickets
    tickets = input("Enter the number ot tickets to sell: /n") 
    try:
        if ((int(tickets) < 1) | (int(tickets) > 1000)):
            print("Invalid number of tickets")
            return
    except:
        print("Invalid number of tickets")
        return
    addToTransactions("SEL " + serviceNumber + " " + tickets + " 00000 **** " + "0")
    return

def changeTicket(account, serviceList, changeCounter):
    #if the agent has already changed more than 20 tickets, leave immediately
    if (account == "agent") and (changeCounter > 20):
        print("agent cannot change more than 20 in a single session")
        return 0
    #gets the current service number    
    currentNumber = input("Enter the current service number: \n")
    if not(currentNumber in serviceList):
        print("invalid service number")
        return 0
    #gets the new destination service number
    newNumber = input("Enter the new service number:\n")
    if not(newNumber in serviceList):
        print("invalid service number")
        return 0
    #gets the number of tickets being changed
    try:
        ticketsChanged = int(input("Enter the number of tickets you are changing: \n"))
    except:
        print("Invalid number")
        return changeCounter
    #if agent, checks for the number of tickets changed
    if (account == "agent"):
        if (ticketsChanged + changeCounter > 20):
            print("agent cannot change more than 20 in a single session")
            return 0
    #checks the current date and adds the trasaction to summary file
    addToTransactions("CHG " + currentNumber + " " + str(ticketsChanged) + " " + newNumber + " **** " + "0")
    return (ticketsChanged) + changeCounter

def main():
    entered = input("Begin session: \n")
    #not allow anything other than login
    while not (entered == "login"):
        entered = input("Login before doing any commands: \n")

    #once typed login, no escape until successful login
    account = input("Enter the login type: \n")
    while not (account == "agent" or account == "planner"):
        account = input("Error, not a valid login type. Try again: \n")

    #at successful login, load valid services list
    service = open(serviceFile, "r")
    line = service.readline().rstrip() #get rid of newline character
    serviceList = []
    while line != "00000":
        serviceList.append(line)
        line = service.readline().rstrip()

    #create an empty transactions file without writing anything
    open(summaryFile, "a").close() #how to handle if already exist??

    #defining counter variables
    changeCounter = 0
    cancelCounter = 0
    #defining dictionary of all services and numbers of tickets changed per service
    cancelDict = {}
    for i in serviceList:
        cancelDict[i] = 0

    while True:
        entered = input("Enter command: \n")

        #accept either service commands or logout
        if (entered == "createservice"):
            createService(account, serviceList)
        elif (entered == "deleteservice"):
            deleted = deleteService(account, serviceList)
            if (deleted is not None):
                serviceList.remove(deleted) #delete service from active
        elif (entered == "sellticket"):
            sellTicket(account, serviceList)
        elif (entered == "cancelticket"):
            cancelCounter = cancelTicket(account, serviceList, cancelCounter, cancelDict)
        elif (entered == "changeticket"):
            changeCounter = changeTicket(account, serviceList, changeCounter)
        elif (entered == "logout"):
            addToTransactions("EOS 00000 0 00000 **** 0")
            #do I need to direct file somewhere?
            break
        else:
            print("Invalid command, try again")

main() #run the program
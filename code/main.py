#front end of bus ticket service, allows commands over list of services, has user interface
#arguments when run are name of input file, and name of output file
#will take the valid services file as input
#will output a transaction summary file
import sys
import datetime

serviceFile = sys.argv[1]
summaryFile = sys.argv[2]

def addToTransactions(transactionCode):
    transaction = open(summaryFile, "a")
    transaction.write(transactionCode)
    transaction.close()


def createService(account, serviceList):
    if (account == "agent"):
        print("agent cannot create services\n")
        return

    newNumber = input("Enter the new service number:\n")
    if (newNumber in serviceList):
        print("invalid service number\n")
        return
    elif (newNumber[:1] == "0" or len(newNumber) != 5):
        print("invalid service number\n")
        return

    date = input("Enter the date of the service(YYYYMMDD):\n")
    if (len(date) > 8):
        print("invalid date\n")
        return
    elif (int(date[0:4]) > 2999 or int(date[0:4]) < 1980):
        print("invalid date\n")
        return
    elif (int(date[4:6]) > 12 or int(date[4:6]) < 1):
        print("invalid date\n")
        return
    elif (int(date[-2:]) > 31 or int(date[-2:]) < 1):
        print("invalid date\n")
        return
    
    name = input("Enter a name for the service (3-39 characters, cannot begin/end with a space):\n")
    if (len(name) > 39 or len(name) < 3):
        print("invalid service name\n")
        return
    elif (name[:1] == " " or name[-1:] == " "):
        print("invalid service name\n")
        return
    
    print("Service successfuly created\n")
    return


def deleteService(account, serviceList):
    if (account == "agent"):
        print("agent cannot delete services\n")
        return
    print("Enter the service number to be deleted:\n")
    service = input()
    if not(service in serviceList):
        print("invalid service number\n")
        return
    elif (newNumber[:1] == "0" | len(newNumber) != 5):
        print("invalid service number\n")
        return
    
    print("Enter the name of the service to be deleted:\n")
    name = input()
    if (len(name) > 39 | len(name) < 3):
        print("invalid service name\n")
        return
    elif (name[:1] == " " | name[-1:] == " "):
        print("invalid service name\n")
        return
    
    addToTransactions("DEL " + service + " 0 00000 " + name + " " + "0")
    return service


def cancelTicket(account, serviceList, cancelCounter, cancelDict):
    serviceNumber = input("Enter a service number: ")
    if (serviceNumber not in serviceList):
        print("Service number not in the valid services list")
        return 0
    tickets = int(input("Enter the number ot tickets to delete: ")) #enter number of tickets 
    #check number of tickets,must be between 1 and 1000
    if (tickets < 1) | (tickets > 1000):
        print("Number of tickets should be between 1 and 1000")
        return 0
    if (account == 'agent'):
        #agent cannot cancel more than 10 tickets per service per session
        if (tickets + cancelDict[serviceNumber] > 10):
            print("Agents are only allowed to delete 10 tickets per service per session")
            return 0
        if (tickets + cancelcount > 20):
            #agents cannot cancel more than 20 tickers in one session
            print("Agents are only allowed to cancel 20 tickets per session")
            return 0

    cancelCounter += tickets

    today = datetime.now()
    addToTransactions("DEL " + cancelaccount + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return cancelCounter


def sellTicket(account, serviceList):
    serviceNumber = input("Enter a service number: ")
    if (serviceNumber not in serviceList):
        print("Invalid service number\n")
        return
    #enter number of tickets
    tickets = input("Enter the number ot tickets to sell: ") 
    if ((int(tickets) < 1) | (int(tickets) > 1000)):
        print("Invalid number of tickets")
        return
    today = datetime.now()
    addToTransactions("SEL " + sellaccount + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return

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

def main():
    entered = input("Begin session: ")
    #not allow anything other than login
    while not (entered == "login"):
        print("Please login before doing any commands")
        entered = input()

    #once typed login, no escape until successful login
    account = input("Enter the login type: ")
    while not (account == "agent" or account == "planner"):
        account = input("Error, not a valid login type. Please try again: ")

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
        entered = input()

        #accept either service commands or logout
        if (entered == "createservice"):
            createService(account, serviceList)
        elif (entered == "deleteservice"):
            deleted = deleteService(account, serviceList)
            serviceList.remove(deleted) #delete service from active
        elif (entered == "sellticket"):
            sellTicket(account, serviceList)
        elif (entered == "cancelticket"):
            cancelCount = cancelTicket(account, serviceList, cancelCounter, cancelDict)
        elif (entered == "changeticket"):
            changeCounter = changeTicket(account, serviceList, changeCounter)
        elif (entered == "logout"):
            addToTransactions("EOS 00000 0 00000 **** 0")
            #do I need to direct file somewhere?
            break
        else:
            print("Invalid command, try again")

main() #run the program
import sys

serviceFile = sys.argv[1]
summaryFile = sys.argv[2]

def addToTransactions(transactionCode):
    transaction = open(summaryFile, "a")
    transaction.write(transactionCode)
    transaction.close()


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
        if entered == "createservice":
            createService(account, serviceList)
        elif entered == "deleteservice":
            deleted = deleteService(account, serviceList)
            serviceList.remove(deleted) #delete service from active
        elif entered == "sellticket":
            sellTicket(account, serviceList)
        elif entered == "cancelticket":
            cancelCount = cancelTicket(account, serviceList, cancelCounter, cancelDict)
        elif entered == "changeticket":
            changeCounter += changeTicket(account, serviceList, changeCounter)
        elif entered == "logout":
            addToTransactions("EOS 00000 0 00000 **** 0")
            #do I need to direct file somewhere?
            break
        else:
            print("Invalid command, try again")

main()
from datetime import datetime

def cancelTicket(account, serviceList, cancelCount, cancelDict):
    #get service number
    serviceNumber = input("Please enter service number: ")
    if serviceNumber not in serviceList:
        #check if the service number is in the valid services list
        print("Service number not in the valid services list")
        return(0)
    print("Please enter the number ot tickets to delet: ")
    try:
        tickets = int(input()) #enter number of tickets
    except:
        tickets = 0
    while(tickets == 0):
        try: #try block to make sure the input is an integer
            tickets = int(input("Invalid input please try again: ")) 
        except:
            pass         
    #check number of tickets,must be between 1 and 1000
    if (tickets < 1) | (tickets > 1000):
        print("Number of tickets should be between 1 and 1000")
        return(0)
    if (account == 'agent'):
        if(serviceNumber in cancelDict):
            #agent cannot cancel more than 10 tickets per service per session
            if(tickets + cancelDict[serviceNumber] > 10):
                print("Agents are only allowed to delete 10 tickets per service per session")
                return(0)
            else:
                cancelCount += tickets
        if(tickets + cancelCount > 20):
            #agents cannot cancel more than 20 tickers in one session
            print("Agents are only allowed to cancel 20 tickets per session")
            return(0)
    today = datetime.now()
    addToTransactions("DEL " + serviceNumber + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return(cancelCount)

def sellTicket(account, serviceList):
    #ask for service number
    serviceNumber = input("Please enter service number: ")
    if serviceNumber not in serviceList:
        print("invalid service number")
        return(0)
    tickets = input("please enter the number ot tickets to sell: ") #enter number of tickets
    if((int(tickets) < 1) | (int(tickets) > 1000)):
        print("invalid number of tickets")
        return(0)
    today = datetime.now()
    addToTransactions("SEL " + serviceNumber + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return
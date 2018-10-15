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
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
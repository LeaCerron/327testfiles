def deleteService(account, serviceList):
    if(account == "agent"):
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
    if(len(name) > 39 | len(name) < 3):
        print("invalid service name\n")
        return
    elif(name[:1] == " " | name[-1:] == " "):
        print("invalid service name\n")
        return
    
    addToTransactions("DEL " + service + " 0 00000 " + name + " " + "0")
    return service

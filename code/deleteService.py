def deleteService(account, serviceList):
    if(account == "agent"):
        print("agent cannot delete services")
        return
    print("Enter the service number to be deleted")
    service = input()
    if not(service in serviceList):
        print("invalid service number")
        return
    elif (newNumber[:1] = "0" | not(newNumber.len = 5):
        print("invalid service number")
        return
    
    print("Enter the name of the service to be deleted")
    name = input()
    elif(name.len > 39 | name.len < 3):
        print("invalid service name")
        return
    elif(name[:1] = " " | name[:-1] = " "):
        print("invalid service name")
        return
    
    addToTransactions("DEL " + service + " 0 00000 " + name + " " + "0")
    return service

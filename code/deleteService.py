def deleteService(account, serviceList):
    if(account == "agent"):
        print("agent cannot delete services")
        return 0;
    print("Enter the service number to be deleted")
    service = input()
    if not(service in serviceList):
        print("invalid service number")
        return 0
    elif (newNumber[:1] = "0" | not(newNumber.len = 5):
        print("invalid service number")
        return 0
    
    print("Enter the name of the service to be deleted")
    name = input()
    elif(name.len > 39 | name.len < 3):
        print("invalid service name")
        return 0
    elif(name[:1] = " " | name[:-1] = " "):
        print("invalid service name")
        return 0
    
    addToTransactions("DEL " + service + " 0 00000 " + name + " " + "0")
    return 1:

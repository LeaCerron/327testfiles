def createService(account, serviceList):
    if(account == "agent"):
        print("agent cannot create services")
        return
    print("Enter the new service number")
    newNumber = input()
    if(newNumber in serviceList):
        print("invalid service number")
        return
    elif (newNumber[:1] = "0" | not(newNumber.len = 5):
        print("invalid service number")
        return
        
    print("Enter the date of the service: YYYYMMDD")
    date = input()
    if(date.len > 8):
        print("invalid date")
        return
    elif(int(date[:4]) > 2999 | int(date[:4]) < 1980):
        print("invalid date")
        return
    elif(int(date[5:6]) > 12 | int(date[5:6]) < 1):
        print("invalid date")
        return
    elif(int(date[7:8]) > 31 | int(date[7:8]) < 1):
        print("invalid date")
        return
    
    print("Enter a name for the service (3-39 characters, cannot begin/end with a space)")
    name = input()
    if(name.len > 39 | name.len < 3):
        print("invalid service name")
        return
    elif(name[:1] = " " | name[:-1] = " "):
        print("invalid service name")
        return
    
    addToTransactions("CRE " + newNumber + " 0 00000 " + name + " " + date)
    return

def createService(account, serviceList):
    if(account == "agent"):
        print("agent cannot create services\n")
        return
    #print("Enter the new service number")
    newNumber = input("Enter the new service number\n")
    if(newNumber in serviceList):
        print("invalid service number\n")
        return
    elif (newNumber[:1] == "0" | len(newNumber) != 5):
        print("invalid service number\n")
        return
        
    #print("Enter the date of the service: YYYYMMDD")
    date = input("Enter the date of the service: YYYYMMDD\n")
    if(date.len > 8):
        print("invalid date\n")
        return
    elif(int(date[:4]) > 2999 | int(date[:4]) < 1980):
        print("invalid date\n")
        return
    elif(int(date[5:6]) > 12 | int(date[5:6]) < 1):
        print("invalid date\n")
        return
    elif(int(date[7:8]) > 31 | int(date[7:8]) < 1):
        print("invalid date\n")
        return
    
    #print("Enter a name for the service (3-39 characters, cannot begin/end with a space)")
    name = input("Enter a name for the service (3-39 characters, cannot begin/end with a space)\n")
    if(name.len > 39 | name.len < 3):
        print("invalid service name\n")
        return
    elif(name[:1] == " " | name[:-1] == " "):
        print("invalid service name\n")
        return
    
    #addToTransactions("CRE " + newNumber + " 0 00000 " + name + " " + date)
    print("Service successfuly created\n")
    return

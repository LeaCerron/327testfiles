def createService(account, serviceList):
    if(account == "agent"):
        print("agent cannot create services\n")
        return
    #print("Enter the new service number")
    newNumber = input("Enter the new service number:\n")
    if(newNumber in serviceList):
        print("invalid service number\n")
        return
    elif (newNumber[:1] == "0" or len(newNumber) != 5):
        print("invalid service number\n")
        return
        
    #print("Enter the date of the service: YYYYMMDD")
    date = input("Enter the date of the service(YYYYMMDD):\n")
    if(len(date) > 8):
        print("invalid date\n")
        return
    elif(int(date[0:4]) > 2999 or int(date[0:4]) < 1980):
        print("invalid date\n")
        return
    elif(int(date[4:6]) > 12 or int(date[4:6]) < 1):
        print("invalid date\n")
        return
    elif(int(date[-2:]) > 31 or int(date[-2:]) < 1):
        print("invalid date\n")
        return
    
    #print("Enter a name for the service (3-39 characters, cannot begin/end with a space)")
    name = input("Enter a name for the service (3-39 characters, cannot begin/end with a space):\n")
    if(len(name) > 39 or len(name) < 3):
        print("invalid service name\n")
        return
    elif(name[:1] == " " or name[:-1] == " "):
        print("invalid service name\n")
        return
    
    #addToTransactions("CRE " + newNumber + " 0 00000 " + name + " " + date)
    print("Service successfuly created\n")
    return

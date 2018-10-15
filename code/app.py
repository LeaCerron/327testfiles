from datetime import datetime

servicenumbers = ["12345",]
cancelcount = 0
serviceDeleteCount = {}

def cancelticket(account, cancelaccount):
    if cancelaccount not in servicenumbers:
        return(0,"invalid service number")
    print("please enter the number ot tickets to delet: ")
    tickets = input() #enter number of tickets
    
    if(account == 'agent'):
        if(cancelaccount in serviceDeleteCount):
            if(tickets + serviceDeleteCount[cancelaccount] > 10):
                return(0,"Deleteing too many tickets")
            else:
                serviceDeleteCount[cancelaccount] = tickets
        if(int(tickets) + cancelcount > 20):
            return(0,"Deleting too many tickets")
    if((int(tickets) < 1) | (int(tickets) > 1000)):
        return(0,"invalid number of tickets")
    today = datetime.now()
    endoffile("DEL " + cancelaccount + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return(tickets)

def sellticket(account, sellaccount):
    if sellaccount not in servicenumbers:
        return(0,"invalid service number")
    print("please enter the number ot tickets to sell: ")
    tickets = input() #enter number of tickets
    if((int(tickets) < 1) | (int(tickets) > 1000)):
        return(0,"invalid number of tickets")
    today = datetime.now()
    endoffile("SEL " + sellaccount + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return(tickets)

def endoffile(string):
    print(string)
    return(1)

def main():
    string = input()
    number = input()
    cancelticket(string,number)

main()
from datetime import datetime

servicenumbers = ["12345",]
cancelcount = 0
serviceDeleteCount = {}

def cancelTicket(account, cancelaccount, cancelcounter, cancelTicketCount):
    if cancelaccount not in servicenumbers:
        print("Service number not in the valid services list")
        return(0)
    print("Please enter the number ot tickets to delet: ")
    try:
        tickets = int(input()) #enter number of tickets
    except:
        tickets = 0
    while(tickets == 0):
        try:
            tickets = int(input("Invalid input please try again: ")) 
        except:
            pass         
    #check number of tickets
    if (tickets < 1) | (tickets > 1000):
        print("Number of tickets should be between 1 and 1000")
        return(0)
    if (account == 'agent'):
        if(cancelaccount in cancelTicketCount):
            if(tickets + cancelTicketCount[cancelaccount] > 10):
                print("Agents are only allowed to delete 10 tickets per service per session")
                return(0)
            else:
                cancelcounter += tickets
        if(tickets + cancelcount > 20):
            print("Agents are only allowed to delete 20 tickets per session")
            return(0)
    today = datetime.now()
    endoffile("DEL " + cancelaccount + " " + tickets + " 00000 **** " + today.strftime("%Y%m%d"))
    return(tickets)

def sellTicket(account, sellaccount):
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
    cancelTicket(string,number)

main()
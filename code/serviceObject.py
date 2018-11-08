services = []
class Service:
    def __init__(self, serviceNumber, ticketsSold, serviceName, serviceDate):
        self.serviceNumber = serviceNumber
        self.serviceCapacity = 30
        self.ticketsSold = ticketsSold
        self.serviceName = serviceName
        self.serviceDate = serviceDate

    def sellTickets(self, tickets):
        if(tickets <= -1):
            raise Exception("selling a negaive number of tickets")
        self.ticketsSold += tickets
        if(self.ticketsSold > self.serviceCapacity):
            raise Exception("service over capacity")

    def cancelTickets(self, tickets):
        self.ticketsSold -= tickets

def changeTickets(service1, service2, tickets):
    service1.ticketsSold += tickets
    service2.ticketsSold -= tickets

def main():
    services.append(Service(10000, 0,'kingston', 12122020))
    services[0].sellTickets(3)
    print(services[0].serviceNumber)
    print(services[0].ticketsSold)
    print(services[0].serviceName)
    print(services[0].serviceDate)
    #to remove an object use 
    #del services[#]

main()
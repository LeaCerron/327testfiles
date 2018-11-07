services = []
#nameing convention for service objects is service# where # is the service # of an object
#eval('service' + str(serviceNum))
class Service:
    def __init__(self, ticketsSold, serviceName, serviceDate):
        self.serviceCapacity = 30
        self.ticketsSold = ticketsSold
        self.serviceName = serviceName
        self.serviceDate = serviceDate

    def sellTickets(self, tickets):
        self.ticketsSold += tickets

    def cancelTickets(self, tickets):
        self.ticketsSold -= tickets

def changeTickets(service1, service2, tickets):
    service1.cancelTickets(tickets)
    service2.sellTickes(tickets)

def main():
    services.append = eval('service' + str(10000))

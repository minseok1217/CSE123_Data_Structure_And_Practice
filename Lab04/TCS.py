from queueADT import *
from random import randint, uniform


class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        self._arriveprob = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self.served = 0

        self._passengers = CircularQueue()
        self._Agents = [None] * numAgents
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i+1)

        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival (  curTime  )
            self._handleBeginService(  curTime  )
            self._handleEndService(  curTime  )
        self.printResult()

    def printResult(self):
        numServed = self._numPassengers - len(self._passengers)
        # print(self._totalWaitTime)
        # print(numServed)
        avgwait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = {}".format(numServed))
        print("Number of passengers remaining in line = {}".format(len(self._passengers)))
        print("The average wait time was {:.2f}minutes.".format(avgwait))

    def _handleArrival(self, curTime):
        prob = uniform(0.0, 1.0)
        if 0.0 <= prob and prob <= self._arriveprob:
            person = passenger(self._numPassengers + 1, curTime)
            self._passengers.enqueue( person )
            self._numPassengers += 1
            print("Time {}: Passenger {} arrived".format(curTime, person.getPID()))

    def _handleBeginService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFree() and not self._passengers.isEmpty() and curTime != self._numMinutes:
                passenger = self._passengers.dequeue()
                self.served += 1
                stoptime = curTime + self._serviceTime
                self._Agents[i].startService(passenger,stoptime)
                # print(curTime)
                # print(passenger.timeArrived())
                self._totalWaitTime += (curTime - passenger.timeArrived())
                print("Time {}: Agent {} started serving passenger {}".format(curTime, self._Agents[i].getAID(), passenger.getPID()))
            i += 1

    def _handleEndService(self, curTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFinished(curTime):
                passenger = self._Agents[i].stopService()
                print("Time {}: Agent {} stopped serving passenger {}".format(curTime, self._Agents[i].getAID(), passenger.getPID()))
            i += 1

class TicketAgent:
    def __init__(self, aID):
        self._aID = aID
        self._passenger = None
        self._stoptime = -1

    def getAID(self):
        return self._passenger is None

    def isFree(self):
        return self._passenger is None

    def isFinished(self, curTime):
        return self._passenger is not None and curTime == self._stopTime

    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        thepassenger = self._passenger
        self._passenger = None
        return thepassenger

class passenger:
    def __init__(self, pID, Arrivaltime):
        self._pID = pID
        self._arrivalTime = Arrivaltime
    def getPID(self):
        return self._pID

    def timeArrived(self):
        return self._arrivalTime
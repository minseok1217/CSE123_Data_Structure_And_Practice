class Node:
    def __init__(self, prev = None, data = None, nxt = None):
        self.prev = prev
        self.data = data
        self.next = nxt
    def __str__(self):
        return str(self.data)
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def getData(self):
        return self.data

    def setData(self,d):
        self.data = d
    def setNext(self,nn):
        self.next =nn
    def setPrev(self, pn):
        self.prev = pn
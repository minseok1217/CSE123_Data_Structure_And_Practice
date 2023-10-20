from DoublyLinkedList import *

class Term:
    def __init__(self, sgn = None, coeff = None, expon = None ):
        self.sgn =sgn
        self.coeff = coeff
        self.expon = expon

    def __str__(self):
        return str(self.sgn) + str(self.coeff) + "x^" + str(self.expon) + ' '

    def getCoeff(self):
        return self.coeff

    def getExpon(self):
        return self.coeff

    def getSyn(self):
        return self.sgn

class SparsePoly(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def add(self, B):
        pass
    def sub(self, B):
        pass
    def getDegree(self):
        pass
    def display(self, msg = ""):
        print("\t",msg,end='')

        Node = self.head

        while Node is not None :
            print(Node, end='')
            Node = Node.getNext()
        print()

    def read(self):
        self.clear()
        while True :
            token = input("input term (syn coef expon): ").split(" ")
            if token[0] == '-1' :
                self.display("The Polynomial: ")
                return
            self.addAt(self.getSize(), Term(token[0], float(token[1]), int(token[2])))
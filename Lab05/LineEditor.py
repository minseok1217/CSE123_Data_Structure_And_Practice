from singlelinkedlist import *

class LineEditor:
    def __init__(self):
        self.list = SinglyLinkedList()

    def runLineEditor(self):
        while True :
            command = input("i - instert, d - delete, r = replace, p - print, l - loadfile, s - writefile, q - quit -> ")
            if command == 'i': self.addLine()
            elif command == 'd': self.deleteLine()
            elif command == 'r': self.replaceLine()
            elif command == 'p': self.printByLine()
            elif command == 'l': self.loadFromFile()
            elif command == 's': self.writeToFile()
            elif command == 'q': return

    def addLine(self):
        pos = int(input(" input the number: "))
        str = input(" input line text")
        self.list.addAt(pos, str)

    def deleteLine(self):
        pos = int(input(" input the number: "))
        self.list.deleteAt(pos)

    def replaceLine(self):
        pos = int(input(" input the number: "))
        str = input("input modified text: ")
        self.list.replaceDataAt(pos, str)

    def printByLine(self):
        self.list.printByLine()

    def loadFromFile(self):
        filename = 'text.txt'
        with open(filename, "r") as infile:
            lines = infile.readlines();
            for line in lines:
                self.list.addAt(self.list.getSize(), line.rstrip('\n'))

    def writeToFile(self):
        filename = 'text.txt'
        with open(filename, 'w') as outfile:
            sz = self.list.getSize()
            print(sz)
            for i in range(sz):
                outfile.write(self.list.getDataAt(i) + '\n')
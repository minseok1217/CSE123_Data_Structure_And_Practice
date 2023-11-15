from Node import *
from queue import Queue
class MorseCodes:
    def __init__(self):
        self.root = Node()
        self.table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
                      ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
                      ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                      ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
                      ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
                      ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
                      ('Y', '-.--'), ('Z', '--..')]

    def makeMorseTree(self):
        for tp in self.table:
            Code = tp[1]
            node = self.root
            for c in Code:
                if c == '.':
                    if node.getLeft() is None:
                        node.setLeft(Node())
                    node = node.getLeft()
                elif c == '-':
                    if node.getRight() is None:
                        node.setRight(Node())
                    node = node.getRight()

            node.setData(tp[0])

    def printMorseTree(self):
        n = self.root
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n = queue.get()
            if n is not None:
                print(n, end = '->')
                queue.put(n.getLeft())
                queue.put(n.getRight())

    def decode(self, code):
        node = self.root
        for c in code :
            if c == '.':
                node = node.getLeft()
            elif c == '-':
                node = node.getRight()
        return node.data

    def encode(self, ch):
        idx = ord(ch) - ord('A')
        return self.table[idx][1]
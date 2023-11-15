from Node import *
from queue import Queue

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def printInOrder(self, msg=' In-Order : '):
        print(msg, end=' ')
        self.inOrder(self.root)
        print('')

    def inOrder(self, n):
        if n is not None:
            self.inOrder(n.getLeft())
            print(n, end="->")
            self.inOrder(n.getRight())

    def printPreOrder(self, msg=' Pre-Order : '):
        print(msg, end=' ')
        self.preOrder(self.root)
        print('')

    def preOrder(self, n):
        if n is not None:
            print(n, end="->")
            self.preOrder(n.getLeft())
            self.preOrder(n.getRight())

    def printPostOrder(self, msg=' Post-Order : '):
        print(msg, end=' ')
        self.postOrder(self.root)
        print()

    def postOrder(self, n):
        if n is not None:
            self.postOrder(n.getLeft())
            self.postOrder(n.getRight())
            print(n, end="->")

    def printLevelOrder(self, msg=' Level-Order : '):
        print(msg, end=' ')
        self.levelOrder(self.root)
        print()

    def levelOrder(self, n):
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n1 = queue.get()
            if n1 is not None:
                print(n1, end='->')
                queue.put(n1.getLeft())
                queue.put(n1.getRight())

    def calcHeight(self,n):
        if n is None:
            return -1
        hleft = self.calcHeight(n.getLeft())
        hright = self.calcHeight(n.getRight())
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def countLeaf(self, n):
        if n is None:
            return 0
        elif self.isLeaf(n):
            return 1
        else:
            return self.countLeaf(n.getLeft()) + self.countLeaf(n.getRight())

    def isLeaf(self, n):
        return n.getLeft() is None and n.getRight() is None

    def countNode(self, n):
        if n is None:
            return 0
        else:
            return 1 + self.countNode(n.getLeft()) + self.countNode(n.getRight())
            #return 1 + self.count_node(n.left + n.right)


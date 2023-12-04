class Node:
    def __init__(self, data=None, left=None, right=None, up = None, down = None):
        self.data = data
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def __str__(self):
        return '(' + str(self.data) + ')'

    def setLeft(self, node): self.left = node
    def setRight(self, node): self.right = node
    def setUp(self, node): self.up = node
    def setDown(self, node): self.down = node
    def setData(self, data): self.data = data

    def getLeft(self): return self.left
    def getRight(self): return self.right

    def getUp(self): return self.up

    def getDown(self): return self.down
    def getData(self): return self.data

    def __eq__(self, other): return self.data == other.data
    def __ne__(self, other): return self.data != other.data
    def __lt__(self, other): return self.data < other.data
    def __gt__(self, other): return self.data > other.data
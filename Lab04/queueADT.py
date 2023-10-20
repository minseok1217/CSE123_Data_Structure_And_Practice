MAX_QSIZE = 10
class CircularQueue :
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self) :
        return self.front == self.rear

    def isFull(self) :
        return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self) : self.front = self.rear

    def __len__(self) :
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def enqueue(self, item) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            return self.items[self.front]

    def peek(self) :
        if not self.isEmpty():
           return self.items[(self.front + 1) % MAX_QSIZE]

    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front + 1 : self.rear+1]
        else :
#            list1 = self.items[self.front+1:MAX_QSIZE]
 #           list2 = self.items[0:self.rear+1]
  #          list = list1 + list2
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]

        print ("[f=%s,r=%d] ==>"%(self.front, self.rear), out)

class CircularDeque(CircularQueue) :
    def __init__(self) :
        super().__init__()

    def addRear(self,item) :
        self.enqueue(item)

    def deleteFront(self) :
        return self.dequeue()

    def getFront(self) :
        return self.peek()

    def addFront(self, item) :
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE

    def deleteRear(self) :
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear -1 + MAX_QSIZE) % MAX_QSIZE
            return item

    def getRear(self) :
        return self.items[self.rear]


class Stack:
        def __init__(self):
            self.top = []

        def __str__(self):
            # return str(self.top[::1])
            return str(self.top)

        def __len__(self):
            return len(self.top)

        def __contains__(self, item):
            return item in self.top

        def push(self, item):
            self.top.append(item)

        def pop(self):
            if not self.isEmpty():
                return self.top.pop(-1)
            else:
                print("Stack is Empty ...")
                exit()

        def peek(self):
            if not self.isEmpty():
                return self.top[-1]
            else:
                print("Stack is Empty ...")
                exit()

        def size(self):
            return len(self.top)

        def display(self):
            return str(self.top[::1])

        def isEmpty(self):
            return len(self.top) == 0

        def clear(self):
            self.top = []

        def find(self, item):
            for i in range(len(self.top)):
                if self.top[i] == item:
                    return i
            return -1

class Node:
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

    def __str__(self):
        return '(' + str(self.data) + ')'

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self, n):
        self.next = n

    def setData(self, d):
        self.data = d

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def addAt(self, pos, elem):
        before = self.getNodeAt(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.next)
            before.next = node

    def deleteAt(self, pos):
        tmp = Node()
        if(self.isEmpty()) or (pos > self.getSize()):
            tmp = None
        elif pos == 0:
            tmp = self.deleteFront()
        elif pos == self.getSize():
            tmp = self.deleteRear()
        else:
            prev = self.getNodeAt(pos-1)
            tmp = prev.next
            prev.next = tmp.next
            tmp.next = None
        return tmp

    def getNodeAt(self, pos):
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node
    def addRear(self, data):
        if self.head is None:
            self.insertFront(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data, None)

    def deleteFront(self):
        tmp = self.head
        if self.head:
            self.head = self.head.next
            tmp.next = None
        return tmp

    def deleteRear(self):
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next

                second_last = tmp
                tmp = tmp.next
                second_last.next = None
        return tmp

    def printList(self, msg = 'singly Linked List : ') -> None:
        print(msg, end = '')
        tmp = self.head
        while tmp:
            print(tmp.data, end = "->")
            tmp = tmp.next
        print('END')

    def __str__(self):
        tmp = self.head
        string_repr = ""
        while tmp:
            string_repr += str(tmp) + "->"
            tmp = tmp.next
        return string_repr + "END"

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node == None:
            return None
        else :
            return node.data

    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data = data

    def isEmpty(self) :
        return self.head == None

    def clear(self):
        self.head = None

    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.getNext()
            count += 1
        return count

    def reverseList(self):
        prev = None
        tmp = self.head

        while tmp:
            next_node = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next_node
        self.head = prev

    def findData(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.next
        return node

    def printByLine(self):
        print("Line Editor")
        node = self.head
        line = 0
        while node is not None:
            # print('[%2d] '%line, end = '')
            print("{} = {}".format(line, node))
            # print(node)
            node = node.next
            line += 1
        print()
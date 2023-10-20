from Node import *

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self): return self.head == None
    def clear(self): self.head = None

    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + "->"
            temp = temp.next

        return string_repr + "END"

    def printList(self,msg='Doubly Linked List: '):
        print(msg, end='')
        tmp = self.head
        while tmp:
            print(tmp,end='->')
            tmp = tmp.next
        print('END')

    def addRear(self, data):
        newNode = Node(None, data, None)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def addFront(self,data):
        newNode = Node(None,data,None)
        if self.head is None:
            self.head = newNode
        else :
            newNode.next = self.head
            if self.head is not None:
                self.head.prev = newNode

            self.head = newNode

    def getNodeAt(self,pos):
        if(pos < 0 or pos > self.getSize()):
            print("Invalid position")
            return None
        temp = self.head
        while pos > 0 and temp != None:
            temp = temp.next
            pos -= 1
        return temp



    def addAt(self, pos, data):

        if pos == self.getSize():
            self.addRear(data)
            return
        if pos == 0:
            self.addFront(data)
            return

        newNode = Node2(None,data,None)
        before = self.getNodeAt(pos-1)
        if before is None:
            print("This node doesn't exist in DLL")
            return
        newNode.next = before.next
        before.next = newNode
        newNode.prev = before
        if newNode.next is not None:
            newNode.next.prev = newNode

    def getSize(self):
        node = self.head;
        count =0;
        while node is not None :
            node = node.next
            count += 1
        return count

    def getDataAt(self,pos):
        node = self.getNodeAt(pos)
        if node == None :
            return None
        else :
            return node.data

    def replaceDataAT(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None :
            node.data

    def deleteFront(self):
        if self.isEmpty():
            print("List is Empty..")
            return None

        temp = self.head

        if(temp.next == temp.prev):
            self.head=None
            return temp
        else :
            self.head = temp.next
            self.head.prev = None
            return temp

    def deleteRear (self):
        if self.isEmpty():
            print("List is Empty..")
            return None

        temp = self.head
        if (temp.next == temp.prev):
            self.head = None
            return temp
        else:
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            return temp

    def deleteAt(self,pos):
        temp = Node2()
        if pos == self.getSize():
            temp = self.deleteRear()
        elif pos == 0:
            temp = self.deleteFront()
        else :
            before = self.getNodeAt(pos-1)
            if before is None:
                print("This node doesn't exist in DLL")
                return

            temp = before.next
            before.next = temp.next
            temp.next.prev = before
            temp.next = None
            temp.prev = None

        return temp


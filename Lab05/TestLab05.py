from singlelinkedlist import *
from LineEditor import *
from DoublyLinkedList import *
from JosephusProblem import *
from CircularLinkedList import *
from polyNomial import *

def testPoly():
    a = SparsePoly()
    b = SparsePoly()
    a.read()
    b.read()
    a.display(" A = ")
    b.display(" B = ")

def testDoublyLinkedList():
    list2 = DoublyLinkedList()
    print (list2.getSize())
    list2.addRear(30)
    list2.addRear(35)
    list2.addFront(47)
    print(list2)
    print(list2.getSize())
    list2.addFront(50)
    list2.addRear(40)
    list2.addFront(55)
    list2.addRear(60)
    list2.addFront(70)
    list2.addRear(80)
    list2.addAt(3,70)
    list2.addAt(3,80)
    print(list2)
    print("deleted -> ", list2.deleteFront())
    print("deleted -> ", list2.deleteRear())
    print("deleted -> ", list2.deleteAt(2))
    print("deleted -> ", list2.deleteAt(2))

def testJosephusProble():
    jp = JosephusProblem(10, 3)
    jp.runJosephus()

def testCirculaLinkedList():
    list = CircularLinkedList()
    print(list.getSize())
    list.addFront(30)
    list.addFront(15)
    print(list.getSize())
    list.addFront(35)
    list.addFront(20)
    list.addFront(22)
    list.addFront(25)
    list.addFront(50)
    list.addRear(150)
    list.addRear(250)
    print(list)
    print("deleted ->", list.deleteFront())
    print(list)
    print("deleted ->", list.deleteRear())
    print(list)
    print("deleted ->", list.deleteAt(3))
    print("position ->", list.findPos(list.head.next), list.head.next)
    print("position ->", list.findPos(list.head), list.head)
    print(list)


def testSinglyLinkedList():
    list = SinglyLinkedList()
    list.addAt(0, 10)
    list.addAt(0, 20)
    list.addAt(1, 30)
    list.addAt(list.getSize(), 40)
    list.addAt(2, 50)
    list.addFront(23)
    list.addRear(25)
    print(list)
    print(list.getSize())
    print(list.getDataAt(2))
    list.replaceDataAt(2, 90)
    print("List after replacing 2nd element :", list)
    print("List after reversing : ",list.reverseList())
    print(list.deleteFront())
    print("List after deleting element from front :", list)
    print(list.deleteRear())
    print("List after deleting element from Rear :", list)
    print(list.deleteAt(2))
    print("List after deleting 2rd element:", list)
    print(list.deleteAt(0))
    print("List after deleting 3rd element:", list)
    list.deleteAt(list.getSize())
    print("List after deleting 3rd element:", list)
    list.clear()
    print(list)


def testNode():
    d = Node(100, None)
    c = Node(99, d)
    b = Node(23, c)
    a = Node(None, b)

    print(a, a.getNext(), a.getNext().getNext(), a.getNext().getNext().getNext())
def main():
    # testNode()
    # testSinglyLinkedList()
    # le = LineEditor()
    # le.runLineEditor()
    # testJosephusProble()
    testCirculaLinkedList()
    # testPoly()



if __name__ == "__main__":
    main()
from Node import *
from bstTree import *
from queue import Queue, LifoQueue
from MorseCodes import *
from BinaryTree import *
from expressionTree import *
from MinHeap import *
from Huffmancodes import *
from wmDictionary import *

def testWmDictionary():
    wmd = Dictionary()
    wmd.runDict()

def testET():
    et = ExpressionTree()
    postfix = "ab+ef*g*-"
    tnode = et.constructTree(postfix)
    print('\n Inorder (infix)')
    et.inOrder(tnode)
    print('\n Inorder (prefix)')
    et.preOrder(tnode)
    print('\n Inorder (postfix)')
    et.postOrder(tnode)
    pf2 = '359++2*'
    tn = et.constructTree(pf2)
    print('\n Inorder (infix)')
    et.inOrder(tn)
    print('\n Inorder (prefix)')
    et.preOrder(tn)
    print('\n Inorder (postfix)')
    et.postOrder(tn)


def testBinarySearchTree() :
    tree = BinarySearchTree()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    print("Tree for data " + str(data))
    for i in data:
        tree.insert_bst(i)
        tree.printInOrder()
    tree.printPreOrder()
    tree.printPostOrder()
    tree.printLevelOrder()
    print(" Nodes = %d" % tree.countNode(tree.root))
    print(" Leaf Nodes = %d" % tree.countLeaf(tree.root))
    print(" Height = %d" % tree.calcHeight(tree.root))
    print(" Maximum = %d" % tree.search_max_bst(tree.root).data)
    print(" Minimum = %d" % tree.search_min_bst(tree.root).data)
    tree.search_bst(26)
    tree.search_bst(25)
    tree.printLevelOrder(" original: LevelOrder: ")
    tree.delete_bst(3)
    tree.printLevelOrder("  casel: < 3 >: LevelOrder: ")
    tree.delete_bst(68);
    tree.printLevelOrder("  case2: < 68 >: LevelOrder: ")
    tree.delete_bst(18);
    tree.printLevelOrder("  case3: < 18 > LevelOrder: ")
    tree.delete_bst(35);
    tree.printLevelOrder("  case3: < 35 > root: LevelOrder: ")
    print(" Nodes = %d" % tree.countNode(tree.root))
    print(" Leaf Nodes = %d" % tree.countLeaf(tree.root))
    print(" Height = %d" % tree.calcHeight(tree.root))
    print(" Maximum = %d" % tree.search_max_bst(tree.root).data)
    print(" Minimum = %d" % tree.search_min_bst(tree.root).data)

def testHuffman():
    text = "sdflasfa"
    hc = Huffman(text)
    hc.printCodes()
def BFS01(n):
    queue = Queue()
    queue.put(n)
    while not queue.empty():
        n = queue.get()
        if n is None:
            print(n, end = '->')
            queue.put(n.getLeft())
            queue.put(n.getRight())

def DFS01(n):
    stack = LifoQueue()
    stack.put(n)
    while not stack.empty():
        n = stack.get()
        if n is not None:
            print(n, end = '->')
            stack.put(n.getLeft())
            stack.put(n.getRight())

def testTree():
    root = Node(14)
    n2 = Node(4); n3 = Node(15); n4 = Node(3); n5 = Node(9)
    n6 = Node(18); n7 = Node(7); n8 = Node(16); n9 = Node(20)
    n10 = Node(5); n11 = Node(17)

    root.setLeft(n2); root.setRight(n3)
    n2.setLeft(n4); n2.setRight(n5)
    n3.setRight(n6)
    n5.setLeft(n7)
    n6.setLeft(n8); n6.setRight(n9)
    n7.setLeft(n10)
    n8.setRight(n11)

    print('\nBreadth First Search........')
    BFS01(root)
    print('\nDepth First Search.....')
    DFS01(root)

    bt = BinaryTree(root)
    bt.printInOrder()
    bt.printPreOrder()
    bt.printPostOrder()
    bt.printLevelOrder()
    print("Tree Height : ", bt.calcHeight(bt.getRoot()))
    print("Leaf count : ", bt.countLeaf(bt.getRoot()))
    print("Size of the Tree : ", bt.countNode(bt.getRoot()))

def testMorseCodes():
    mc = MorseCodes()
    mc.makeMorseTree()
    mc.printMorseTree()

    str01 = "MUHAMADTARIQMAHMOOD"
    mlist = []
    for ch in str01:
        code = mc.encode(ch)
        mlist.append(code)
    print("Morse Code: ", mlist)
    print("Decoding    ", end = '')
    for code in mlist:
        ch = mc.decode(code)
        print(ch, end= '')
    print()

def testNode():
    root = Node(14)
    n2 = Node(4); n3 = Node(15); n4 = Node(3); n5 = Node(9)
    n6 = Node(18); n7 = Node(7); n8 = Node(16); n9 = Node(20)
    n10 = Node(5); n11 = Node(17)

def testMinHeap():
    print("\n Heap Test")

    heap = MinHeap()
    data = [2, 5, 4, 8, 9, 3, 7, 3]
    print("Data elements : " + str(data))

    for elem in data:
        heap.insert(elem)
    heap.printHeap()
    print(heap)

    heap.delete()
    heap.printHeap()
    print(heap)

    heap.delete()
    heap.printHeap()
    print(heap)

def testHuffman():
    text = "kjalklkkjaklkllkfkljsdkl"
    hc = Huffman(text)

    freq=hc.makeFrequencyDict()
    for key in freq:
        print("{} : {}".format(key, freq[key]))
    hc.printCodes()


def main():
    testMorseCodes()
    # testHuffman()
    # testET()
    # testBinarySearchTree()
    # testWmDictionary()
    # testTree()
    # testMinHeap()


if __name__ == "__main__":
    main()

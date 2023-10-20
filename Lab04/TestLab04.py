from queueADT import *
from MediaPlayer import *
from TCS import *
from Maze import *

def runSimulation():
    done = TicketCounterSimulation(5, 30, 2,3)
    done.run()

def testMPQ():
    track1 = Track("white whistle")
    track2 = Track("butter butter")
    track3 = Track("Oh black star")
    track4 = Track("Watch that chicken")
    track5 = Track("don't go")
    mp = MediaPlayerQueue()
    mp.add_track(track1)
    mp.add_track(track2)
    mp.add_track(track3)
    mp.add_track(track4)
    mp.add_track(track5)
    mp.play()

def testCIrcularQueue() :
    print ('Test Queue')
    q = CircularQueue()
    for i in range(10) :
        q.enqueue(i)
    print('   enqueue()x9:  ',end = '')
    q.print()
    print("    dequeue()-->", q.dequeue())
    print("    dequeue()-->", q.dequeue())
    print("    dequeue()-->", q.dequeue())
    print("   dequeue()x3:  ", end = '')

    q.clear()
    q.enqueue('aaa')
    q.enqueue('bbb')
    q.enqueue('ccc')
    q.enqueue('ddd')
    print('   enqueue()x4:  ', end = '')
    q.print()
    print("    dequeue()-->", q.dequeue())
    print('   dequeue()x9  ', end='')
    q.print()
    print('    peek()-->', q.peek())
    print('\n')

def testCircularDeque() :
    print('Deque Test')
    q = CircularDeque()
    for i in range(10):
        q.enqueue(i)
    print('   enqueue()x9:  ', end='')
    q.print()
    print("    dequeue()-->", q.deleteFront())
    print("    dequeue()-->", q.deleteFront())
    print("    dequeue()-->", q.deleteFront())
    print("    dequeue()-->", q.deleteRear())
    print("    dequeue()-->", q.deleteRear())
    print("   dequeue()x3:  ", end='')
    q.print()

    q.clear()
    q.addRear('aaa')
    q.addRear('bbb')
    q.addRear('ccc')
    q.addRear('ddd')
    print('   enqueue()x4:  ', end='')
    q.print()
    print("    dequeue()-->", q.deleteRear())
    print('   dequeue()x9  ', end='')
    q.print()
    print('    peek()-->', q.getFront())
    print('    peek()-->', q.getRear())
    print('\n')

def useMaze():
    m = Maze()
    m.DFS1()
    m.DFS2()
    m.DFS3()
    m.BFS1()
    m.BFS2()

def main():
    # testCIrcularQueue()
    # testCircularDeque()
    # testMPQ()
    useMaze()
    # runSimulation()
if (__name__ == "__main__"):
    main()
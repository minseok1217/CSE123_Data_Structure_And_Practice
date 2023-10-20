from queueADT import *

class Cell:
    def __init__(self, r = 0, c = 0):
        self.row = r
        self.col = c
    def __str__(self):
        return "("+ str(self.row) + ", " + str(self.col) +")"
class Maze:
    MAZE_SIZE = 6
    def getMap(self):
        map = [['1', '1', '1', '1', '1', '1'],
               ['e', '0', '1', '0', '0', '1'],
               ['1', '0', '0', '0', '1', '1'],
               ['1', '0', '1', '0', '1', '1'],
               ['1', '0', '1', '0', '0', 'x'],
               ['1', '1', '1', '1', '1', '1']]
        return map
    def isValidPos(self,x,y,map):
        if(x < 0 or y < 0 or x >= self.MAZE_SIZE or y >= self.MAZE_SIZE):
            return False
        else:
            return map[y][x] == '0' or map[y][x] == 'x'

    def DFS1(self):
        map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addFront(entry)
        print('\n DFS1 : using Deque Data Structure:')

        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end='->')
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map) : deq.addFront(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.addFront(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.addFront(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.addFront(Cell(x, y + 1))
        return False
    def DFS2(self):
        map = self.getMap()
        s = Stack()
        entry = Cell(0, 1)
        s.push(entry)
        print('\n DFS2 : using Stack Data Structure:')

        while not s.isEmpty():
            here = s.pop()
            print(here, end='->')
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map) : s.push(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): s.push(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): s.push(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): s.push(Cell(x, y + 1))
        return False
    def DFS3(self):
        map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print('\n DFS3 : using Deque Data Structure:')

        while not deq.isEmpty():
            here = deq.deleteRear()
            print(here, end='->')
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map) : deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.addRear(Cell(x, y + 1))
        return False
    def BFS1(self):
        map = self.getMap()
        deq = CircularDeque()
        entry = Cell(0, 1)
        deq.addRear(entry)
        print('\n BFS1 : using Deque Data Structure:')
        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end='->')
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map): deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.addRear(Cell(x, y + 1))
        return False
    def BFS2(self):
        map = self.getMap()
        deq = CircularQueue()
        entry = Cell(0, 1)
        deq.enqueue(entry)
        print('\n BFS2 : using Queue Data Structure:')
        while not deq.isEmpty():
            here = deq.dequeue()
            print(here, end='->')
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map): deq.enqueue(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.enqueue(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.enqueue(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.enqueue(Cell(x, y + 1))
        return False

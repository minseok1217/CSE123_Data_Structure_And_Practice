from queue import Queue, LifoQueue
from Graph import Graph
from collections import defaultdict


class SearchGraph:

    def bfs(self, adjlist, start):
        visited = set()
        print("BFS starting with Vertex", start)
        visited.add(start)
        q = Queue()
        q.put(start)
        while not q.empty():
            v = q.get()
            print(v, end='->')
            nbr = adjlist[v]
            for u in nbr:
                if u not in visited:
                    visited.add(u)
                    q.put(u)
        print()

    def dfs(self, adjList, start):
        visited = set()
        print("DFS starting with Vertex", start)
        visited.add(start)
        s = LifoQueue()
        s.put(start)
        while not s.empty():
            v = s.get()
            print(v, end='->')
            nbr = adjList[v]
            for u in nbr:
                if u not in visited:
                    visited.add(u)
                    s.put(u)
        print()

    def doTS(self, adjList):
        visited = defaultdict()
        for vtx in adjList:
            visited[vtx] = False
        result = []
        for v in visited:
            self.dfsTS(v, adjList, visited, result)
        print(result)

    def dfsTS(self, v, adjList, visited, result):
        if not visited[v]:
            visited[v] = True
            for n in adjList[v]:
                self.dfsTS(n, adjList, visited, result)
            result.insert(0, v)

    def findCC(self, adjList):
        visited = set()
        colorList = []
        for v in adjList:
            if v not in visited:
                color = self.dfsCC(adjList, [], v, visited)
                colorList.append(color)
        print("Connected Components = {}".format(len(colorList)))
        print(colorList)
        print()

    def dfsCC(self, adjList, color, v, visited):
        if v not in visited:
            visited.add(v)
            color.append(v)
            n = adjList[v]
            for vtx in n:
                if vtx not in visited:
                    self.dfsCC(adjList, color, vtx, visited)
        return color


class EightQueen:
    def __init__(self, NQ):
        self.NQ = NQ
        self.solutions = 0
        self.nn = 0

    def solve(self):
        board = [-1] * self.NQ
        self.dfsPQ(board, 0)
        print("Found", self.solutions, "solutions.")
        print("Node Visited = ", self.nn, "solutions.")

    def dfsPQ(self, board, row):
        if row == self.NQ:
            print(board)
            self.solutions += 1

        else:
            for col in range(self.NQ):
                if not self.isAttack(board, row, col):
                    self.nn += 1
                    board[row] = col
                    self.dfsPQ(board, row + 1)

    def isAttack(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return True
        return False

from queue import Queue, LifoQueue
# from Graph import Graph
from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge1(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = None
            self.vertices[vertex2][vertex1] = None

    def add_edge2(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex][end_vertex] = weight

    def add_edge3(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight

    def display1(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex} --- {', '.join(neighbors)}")

    def display2(self):
        for vertex, neighbors in self.vertices.items():
            for neighbor, weight in neighbors.items():
                print(f"{vertex} -> {neighbor} : {weight}")

    def display3(self):
        for vertex, neighbors in self.vertices.items():
            for neighbor, weight in neighbors.items():
                print(f"{vertex} --- {neighbor} : {weight}")

    def getGraphs():
        graph1 = Graph()
        return graph1
        

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
    
# Creating Graph objects
graph1 = Graph()
graph2 = Graph()
graph3 = Graph()

# Adding vertices and edges for Figure 1
graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C")
graph1.add_vertex("D")
graph1.add_vertex("E")
graph1.add_vertex("F")
graph1.add_vertex("G")
graph1.add_vertex("H")
graph1.add_edge1("A", "C")
graph1.add_edge1("A", "B")
graph1.add_edge1("C", "D")
graph1.add_edge1("C", "E")
graph1.add_edge1("B", "D")
graph1.add_edge1("D", "F")
graph1.add_edge1("E", "G")
graph1.add_edge1("E", "H")
graph1.add_edge1("G", "H")

# Adding vertices and edges for Figure 2
graph2.add_vertex("v1")
graph2.add_vertex("v2")
graph2.add_vertex("v3")
graph2.add_vertex("v4")
graph2.add_vertex("v5")
graph2.add_vertex("v6")
graph2.add_vertex("v7")

graph2.add_edge2("v1", "v2", 4)
graph2.add_edge2("v2", "v1", 3)
graph2.add_edge2("v1", "v6", 10)
graph2.add_edge2("v2", "v4", 18)
graph2.add_edge2("v4", "v2", 5)
graph2.add_edge2("v4", "v6", 19)
graph2.add_edge2("v4", "v7", 5)
graph2.add_edge2("v7", "v4", 8)
graph2.add_edge2("v6", "v7", 10)
graph2.add_edge2("v3", "v2", 6)
graph2.add_edge2("v4", "v3", 15)
graph2.add_edge2("v4", "v5", 2)
graph2.add_edge2("v5", "v4", 1)
graph2.add_edge2("v5", "v3", 12)

# Adding vertices and edges for Figure 3
graph3.add_vertex("v1")
graph3.add_vertex("v2")
graph3.add_vertex("v3")
graph3.add_vertex("v4")
graph3.add_vertex("v5")
graph3.add_vertex("v6")
graph3.add_vertex("v7")
graph3.add_edge3("v1", "v2", 2)
graph3.add_edge3("v1", "v3", 4)
graph3.add_edge3("v1", "v4", 1)
graph3.add_edge3("v4", "v6", 8)
graph3.add_edge3("v4", "v7", 4)
graph3.add_edge3("v4", "v5", 7)
graph3.add_edge3("v4", "v2", 3)
graph3.add_edge3("v3", "v6", 5)
graph3.add_edge3("v6", "v7", 1)
graph3.add_edge3("v7", "v5", 6)
graph3.add_edge3("v5", "v2", 10)
graph3.add_edge3("v2", "v1", 2)

# Displaying the graphs
print("Graph 1:")
graph1.display1()

print("\nGraph 2:")
graph2.display2()

print("\nGraph 3:")
graph3.display3()

def useSearchGraph():

    print("Figures 1 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = graph1
    aL1 = g.getAdjList()
    sv = g.getVertexList()[0]

    print(sv)

    sg.dfs(aL1, sv)
    sg.bfs(aL1, sv)
    print()

    print("Figures 2 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = graph2
    aL2 = g.getAdjList()
    sv = g.getVertexList()[0]

    sg.dfs(aL2, sv)
    sg.bfs(aL2, sv)
    print()

    print("Figures 3 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = graph3
    aL3 = g.getAdjList()
    sv = g.getVertexList()[0]

    sg.dfs(aL3, sv)
    sg.bfs(aL3, sv)
    print()

    print("Figures 1 : ", end='')
    sg.doTS(aL1)
    print("Figures 2 : ", end='')
    sg.doTS(aL2)
    print("FiDDgures 3 : ", end='')
    sg.doTS(aL3)

    print("Figures 1 : ", end='')
    sg.findCC(aL1)
    print("Figures 2 : ", end='')
    sg.findCC(aL2)
    print("Figures 3 : ", end='')
    sg.findCC(aL3)

    eq = EightQueen(6)
    eq.solve()
    print()
    
def main():
    useSearchGraph()

if __name__ == "__main__":
    main()
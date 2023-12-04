from Graph import Graph
from queue import PriorityQueue


class Dijkstra:
    def runDijkstra(self, G, src):
        Known = {}
        Dv = {}
        Pv = {}
        for vtx in G.getVertexList():
            Known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None

        Known[src] = False
        Dv[src] = 0.0
        PQ = PriorityQueue()
        PQ.put((0, src))

        while not PQ.empty():
            self.printConfigration(Known, Dv, Pv)
            emin = PQ.get()[1]
            for e in G.getNeighborEdges(emin):
                EdgeDistance = e.getW()
                newDistance = Dv[e.getU()]+EdgeDistance
                if (not Known[e.getV()]) and Dv[e.getV()] > newDistance:
                    Dv[e.getV()] = newDistance
                    Pv[e.getV()] = e.getU()
                    PQ.put((newDistance, e.getV()))
                Known[e.getU()] = True

    def printConfigration(self, Known, Dv, Pv):
        print("Configration")
        for vtx in Known:
            print("{}, {}, {}, {}".format(vtx, Known[vtx],Dv[vtx], Pv[vtx]))


class MST:
    def mstKruskal(self, G):
        T = Graph(G.isDirected())
        for v in G.getVertexList():
            T.addVertex(v)
        ds = DS()
        for v in G.getVertexList():
            ds.makeSet(v)
        pq = PriorityQueue()
        for e in G.getEdges():
            pq.put(e)
        noe = 0
        while not pq.empty():
            e = pq.get()
            p1 = ds.find(e.getU())
            p2 = ds.find(e.getV())
            if p1 != p2:
                T.addEdge(e)
                ds.union(p1, p2)
                noe += 1
        return T

    def mstPrim(self, G, src):
        T = Graph(G.isDirected())
        eList = []
        PQ = PriorityQueue()
        for e in G.getNeighborEdges(src):
            PQ.put(e)
        T.addVertex(src)

        while T.getOrder() != G.getOrder():
            minE = PQ.get()
            vtxV = minE.getV()
            if vtxV in T.getVertexList():
                continue

            T.addVertex(vtxV)
            T.addEdge(minE)
            eList.append(minE)
            for e in G.getNeighborEdges(vtxV):
                PQ.put(e)

        return T


class DS:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def makeSet(self, v):
        self.parent[v] = v
        self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root1] += 1


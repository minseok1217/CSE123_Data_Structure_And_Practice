from collections import OrderedDict

class Graph:
    def __init__(self, directed=False, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        self.Directed = directed
        self.keyIndex = {}

    def isDirected(self):
        return self.Directed

    def getVertexList(self):
        dict1 = OrderedDict(sorted(self.keyIndex.items()))
        return list(dict1.keys())

    def getOrder(self):
        return len(self.getVertexList())
    def getSize(self):
        pass
    def getVertexDegree(self):
        pass
    def getDegree(self):
        pass

    def getNeighbors(self, v):
        nList = []
        eList = self.gdict.get(v)
        for e in eList:
            nList.append(e.getV())
        return nList

    def getNeighborVertices(self, vtx):
        elist = self.gdict.get(vtx)
        vlist = []
        for e in elist:
            vlist.append(e.getV())
        return vlist

    def getNeighborEdges(self, vtx):
        return self.gdict[vtx]

    def getAdjList(self):
        aList = {}
        for vtx in self.gdict:
            aList[vtx] = set(self.getNeighbors(vtx))
        return aList

    def printAdjList(self):
        aList = self.getAdjList()
        for vtx in aList:
            print("{} : {} ".format(vtx, aList[vtx]))

    def getEdges(self):
        eList = []
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                eList.append(e)
        return sorted(eList)

    def getAdjMat(self):
        adjMat = [[0 for x in range(len(self.keyIndex))] for y in range(len(self.keyIndex))]
        for e in self.getEdges():
            adjMat[self.keyIndex[e.getU()]-1][self.keyIndex[e.getV()]-1] = e.getW()
        return adjMat

    def __repr__(self):
        gs = ""
        for vtx in self.gdict:
            gs += "{} : {} \n".format(vtx, self.gdict[vtx])
        return gs

    def __str__(self):
        gs=""
        for vtx in self.gdict:
            gs += "{} : {} \n".format(vtx, self.gdict[vtx])
        return gs

    def addVertex(self, vtx):
        if vtx in self.gdict.keys():
            print("Vertex is already added..")
        else:
            self.gdict[vtx] = []
            self.keyIndex[vtx] = len(self.keyIndex) + 1

    def addEdge(self, e):
        if e.getU() in self.gdict:
            self.gdict[e.getU()].append(e)
        #if (not self.Directed):
            #e2 = Edge(e.getV(), e.getU(), e.getW())
            #self.gdict[e.getV()].append(e2)


class Edge:
    def __init__(self,u=None,v=None,w=None):
        self.u = u
        self.v = v
        self.w = w

    def getU(self):
        return self.u

    def getV(self):
        return self.v

    def getW(self):
        return self.w

    def __str__(self):
        return '(' + str(self.u) + ',' + str(self.v) + ')->' + str(self.w)

    def __repr__(self):
        return '(' + str(self.u) + ',' + str(self.v) + ')->' + str(self.w)

    def __hash__(self):
        return hash(self.w)

    def __eq__(self, other):
        return self.w == other.w

    def __ne__(self, other):
        return self.w != other.w

    def __lt__(self, other):
        return self.w < other.w

    def __le__(self, other):
        return self.w <= other.w

    def __gt__(self, other):
        return self.w > other.w

    def __ge__(self, other):
        return self.w >= other.w


class Vertex:
    def __init__(self, key=None):
        self.key = key

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def setData(self, k):
        self.key = k

    def getData(self):
        return self.key

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

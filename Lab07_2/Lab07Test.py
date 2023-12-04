import MST
from getGraphs import getGraphs
from SearchGraph import SearchGraph, EightQueen
from MST import MST, Dijkstra

def useDijkstra():
    gg = getGraphs()
    g = gg.getG3()
    print(g)
    sv = g.getVertexList()[0]
    dk = Dijkstra()
    dk.runDijkstra(g, sv)

    #T2 = mst.runPrim(g, sv)

def useMst():
    mst = MST()
    gg = getGraphs()
    g = gg.getG2()
    print(g.getEdges())
    print()
    T1 = mst.mstKruskal(g)
    print(T1)
    print("Kruskal : ", end='')
    print(T1.getEdges())
    print()

    sv = g.getVertexList()[0]
    T2 = mst.mstPrim(g, sv)
    print("Prim : ", end='')
    print(T2.getEdges())

def useSearchGraph():

    print("Figures 1 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = gg.getG1()
    aL1 = g.getAdjList()
    sv = g.getVertexList()[0]

    print(sv)

    sg.dfs(aL1, sv)
    sg.bfs(aL1, sv)
    print()

    print("Figures 2 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = gg.getG2()
    aL2 = g.getAdjList()
    sv = g.getVertexList()[0]

    sg.dfs(aL2, sv)
    sg.bfs(aL2, sv)
    print()

    print("Figures 3 : ")
    sg = SearchGraph()
    gg = getGraphs()
    g = gg.getG3()
    aL3 = g.getAdjList()
    sv = g.getVertexList()[0]

    sg.dfs(aL3, sv)
    sg.bfs(aL3, sv)
    print()

    print("Figures 1 : ", end='')
    sg.doTS(aL1)
    print("Figures 2 : ", end='')
    sg.doTS(aL2)
    print("Figures 3 : ", end='')
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

def G3Test():
    gg = getGraphs()
    g = gg.getG3()
    print(g)

    print(g.getEdges())
    M=g.getAdjMat()

    for i in M:
        print(i)
    g.printAdjList()

def G2Test():
    gg = getGraphs()
    g = gg.getG2()
    print(g)

    print(g.getEdges())
    M=g.getAdjMat()

    for i in M:
        print(i)
    g.printAdjList()

def G1Test():
    gg = getGraphs()
    g = gg.getG1()
    print(g)

    print(g.getEdges())
    M=g.getAdjMat()

    for i in M:
        print(i)
    g.printAdjList()


def main():
    #G1Test()
    #G2Test()
    #G3Test()
    #useSearchGraph()
    #useMst()
    useDijkstra()

if __name__ == '__main__':
    main()
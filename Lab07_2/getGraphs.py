from Graph import *
from SearchGraph import *

class getGraphs:
    def getG1(self):
        sg = SearchGraph()

        g = Graph(False)
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")
        v6 = Vertex("F")
        v7 = Vertex("G")
        v8 = Vertex("H")

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)
        g.addVertex(v6)
        g.addVertex(v7)
        g.addVertex(v8)

        e1 = Edge(v1, v2, 1)
        e2 = Edge(v1, v3, 1)
        e3 = Edge(v2, v4, 1)
        e4 = Edge(v3, v4, 1)
        e5 = Edge(v3, v5, 1)
        e6 = Edge(v4, v6, 1)
        e7 = Edge(v5, v7, 1)
        e8 = Edge(v5, v8, 1)
        e9 = Edge(v7, v8, 1)

        g.addEdge(e1)
        g.addEdge(e2)
        g.addEdge(e3)
        g.addEdge(e4)
        g.addEdge(e5)
        g.addEdge(e6)
        g.addEdge(e7)
        g.addEdge(e8)
        g.addEdge(e9)

        return g

    def getG2(self):
        sg = SearchGraph()

        g = Graph(False)
        v1 = Vertex("v1")
        v2 = Vertex("v2")
        v3 = Vertex("v3")
        v4 = Vertex("v4")
        v5 = Vertex("v5")
        v6 = Vertex("v6")
        v7 = Vertex("v7")

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)
        g.addVertex(v6)
        g.addVertex(v7)

        e12 = Edge(v1, v2, 2); e13 = Edge(v1, v3, 4); e14 = Edge(v1, v4, 1)
        e21 = Edge(v2, v1, 2); e24 = Edge(v2, v4, 3); e25 = Edge(v2, v5, 10);
        e31 = Edge(v3, v1, 4); e34 = Edge(v3, v4, 2); e36 = Edge(v4, v6, 5);
        e41 = Edge(v4, v1, 1); e42 = Edge(v4, v2, 3); e43 = Edge(v4, v3, 2);
        e45 = Edge(v4, v5, 7); e46 = Edge(v4, v6, 8); e47 = Edge(v4, v7, 4);
        e52 = Edge(v5, v2, 10); e54 = Edge(v5, v4, 7); e57 = Edge(v5, v7, 6);
        e63 = Edge(v6, v3, 5); e64 = Edge(v6, v4, 8); e67 = Edge(v6, v7, 1);
        e74 = Edge(v7, v4, 4); e75 = Edge(v7, v5, 6); e76 = Edge(v7, v6, 1);

        g.addEdge(e12); g.addEdge(e13); g.addEdge(e14)
        g.addEdge(e21); g.addEdge(e24); g.addEdge(e25)
        g.addEdge(e31); g.addEdge(e34); g.addEdge(e36)
        g.addEdge(e41); g.addEdge(e42); g.addEdge(e43)
        g.addEdge(e45); g.addEdge(e46); g.addEdge(e47)
        g.addEdge(e52); g.addEdge(e54); g.addEdge(e57)
        g.addEdge(e63); g.addEdge(e64); g.addEdge(e67)
        g.addEdge(e74); g.addEdge(e75); g.addEdge(e76)

        return g

    def getG3(self):
        sg = SearchGraph()

        g = Graph(False)
        v1 = Vertex("v1")
        v2 = Vertex("v2")
        v3 = Vertex("v3")
        v4 = Vertex("v4")
        v5 = Vertex("v5")
        v6 = Vertex("v6")
        v7 = Vertex("v7")

        g.addVertex(v1)
        g.addVertex(v2)
        g.addVertex(v3)
        g.addVertex(v4)
        g.addVertex(v5)
        g.addVertex(v6)
        g.addVertex(v7)

        e12 = Edge(v1, v2, 4); e16 = Edge(v1, v6, 10);
        e21 = Edge(v2, v1, 3); e24 = Edge(v2, v4, 18);
        e32 = Edge(v3, v2, 6);
        e42 = Edge(v4, v2, 5); e43 = Edge(v4, v3, 15); e45 = Edge(v4, v5, 2);
        e46 = Edge(v4, v6, 19); e47 = Edge(v4, v7, 5);
        e53 = Edge(v5, v3, 12); e54 = Edge(v5, v4, 1);
        e67 = Edge(v6, v7, 10);
        e74 = Edge(v7, v4, 8);

        g.addEdge(e12); g.addEdge(e16);
        g.addEdge(e21); g.addEdge(e24);
        g.addEdge(e32);
        g.addEdge(e42); g.addEdge(e43); g.addEdge(e45);
        g.addEdge(e46); g.addEdge(e47)
        g.addEdge(e53); g.addEdge(e54);
        g.addEdge(e67);
        g.addEdge(e74);

        return g

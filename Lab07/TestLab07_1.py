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
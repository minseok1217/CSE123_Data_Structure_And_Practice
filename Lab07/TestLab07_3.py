class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge2(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex][end_vertex] = weight
            self.vertices[end_vertex][start_vertex] = weight  # 무방향 그래프이므로 양방향으로 추가

    def display2(self):
        for vertex, neighbors in self.vertices.items():
            for neighbor, weight in neighbors.items():
                print(f"{vertex} -> {neighbor} : {weight}")


def prims_algorithm(graph):
    result = []
    key = {vertex: float('inf') for vertex in graph.vertices}
    parent = {vertex: None for vertex in graph.vertices}
    start_vertex = list(graph.vertices.keys())[0]
    key[start_vertex] = 0

    for _ in range(len(graph.vertices)):
        u = min(key, key=key.get)
        key[u] = float('inf')  # 방문한 정점은 더 이상 고려하지 않음

        for v, weight in graph.vertices[u].items():
            if v in key and weight < key[v]:
                key[v] = weight
                parent[v] = u

    for v, u in parent.items():
        if u is not None:
            result.append((u, v, graph.vertices[u][v]))

    return result


def kruskals_algorithm(graph):
    result = []
    edges = []

    for vertex, neighbors in graph.vertices.items():
        for neighbor, weight in neighbors.items():
            edges.append((vertex, neighbor, weight))

    edges = sorted(edges, key=lambda x: x[2])
    parent = {vertex: vertex for vertex in graph.vertices}

    def find_set(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_set(parent[vertex])
        return parent[vertex]

    def union_sets(u, v):
        root_u = find_set(u)
        root_v = find_set(v)
        parent[root_u] = root_v

    for edge in edges:
        u, v, weight = edge
        if find_set(u) != find_set(v):
            result.append((u, v, weight))
            union_sets(u, v)

    return result


# 그래프 생성 및 테스트
graph2 = Graph()
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

print("Prim's Algorithm 결과:")
result_prim = prims_algorithm(graph2)
for edge in result_prim:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")

print("\nKruskal's Algorithm 결과:")
result_kruskal = kruskals_algorithm(graph2)
for edge in result_kruskal:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
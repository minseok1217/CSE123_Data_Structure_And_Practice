import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge3(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight

    def display3(self):
        for vertex, neighbors in self.vertices.items():
            for neighbor, weight in neighbors.items():
                print(f"{vertex} --- {neighbor} : {weight}")


def dijkstra_algorithm(graph, start_vertex):
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Figure 3의 그래프로 테스트
graph3 = Graph()
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

print("Dijkstra Algorithm 결과:")
start_vertex = "v1"
result_dijkstra = dijkstra_algorithm(graph3, start_vertex)
for vertex, distance in result_dijkstra.items():
    print(f"{start_vertex}에서 {vertex}까지의 최단 경로 거리: {distance}")
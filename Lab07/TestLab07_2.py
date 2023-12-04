from collections import deque

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

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.vertices[vertex] if neighbor not in visited)
    
    def connected_components(graph):
        visited = set()
        components = []
        for vertex in graph.vertices:
            if vertex not in visited:
                component = []
                graph._dfs_recursive_connected_components(vertex, visited, component)
                components.append(component)
        return components

    # Graph 클래스에 연결 요소 구하는 보조 함수 추가
    def _dfs_recursive_connected_components(self, vertex, visited, component):
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            for neighbor in self.vertices[vertex]:
                self._dfs_recursive_connected_components(neighbor, visited, component)

    def topological_sort(graph):
        visited = set()
        stack = []
        for vertex in graph.vertices:
            if vertex not in visited:
                graph._dfs_recursive_topological_sort(vertex, visited, stack)
        return stack[::-1]

    # Graph 클래스에 위상 정렬을 위한 보조 함수 추가
    def _dfs_recursive_topological_sort(self, vertex, visited, stack):
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                self._dfs_recursive_topological_sort(neighbor, visited, stack)
            stack.append(vertex)

    def n_queens(n):
        def is_safe(board, row, col):
            # Check in the same column
            for i in range(row):
                if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    return False
            return True

def solve_queens(board, row):
    if row == n:
        solutions.append(board[:])  # Found a solution
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(board, row + 1)

    solutions = []
    solve_queens([0] * n, 0)
    return solutions

def n_queens(n):
    def is_safe(board, row, col):
        # Check in the same column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

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

# 그래프 객체 생성 및 DFS, BFS 테스트
print("DFS on Graph 1:")
graph1.bfs("A")


print("\nBFS on Graph 2:")
graph2.bfs("v1")

n_queens_solutions = n_queens(4)
print("\nSolutions for N-Queens Problem (N=4):")
for solution in n_queens_solutions:
    print(solution)
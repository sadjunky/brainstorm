# Graph traversal using BFS algortithm
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, x, y):
        self.graph[x].append(y)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []
        queue.insert(0, start)
        visited[start] = True

        while queue:
            pos = queue.pop()
            print(pos, end=" ")

            for vertex in self.graph[pos]:
                if not visited[vertex]:
                    visited[vertex] = True
                    queue.insert(0, vertex)
                
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)

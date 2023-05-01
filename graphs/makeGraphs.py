
from collections import defaultdict
import random


class Graph:

    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # * Recursive DFS *
    # * Generates error when recursion limit is reached *
    # def DFSUtil(self, v, visited):
    #     # Mark the current node as visited
    #     visited[v] = True

    #     # Recur for all the vertices adjacent to this vertex
    #     for i in self.graph[v]:
    #         if visited[i] == False:
    #             self.DFSUtil(i, visited)

    def DFSUtil(self, v, visited):
        # Create a stack for DFS
        stack = []
        # Push the current node to the stack
        stack.append(v)

        while stack:
            # Pop a vertex from stack and print it
            v = stack.pop()

            # If the vertex is not visited, mark it as visited
            if not visited[v]:
                visited[v] = True

            # Get all adjacent vertices of the popped vertex
            # If an adjacent vertex is not visited, then push it to the stack
            for i in self.graph[v]:
                if not visited[i]:
                    stack.append(i)

    def isConnected(self):

        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        #  Find a vertex with non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) == 0:
                return False

        # Start DFS traversal from a vertex with non-zero degree
        self.DFSUtil(0, visited)

        # Check if all non-zero degree vertices are visited
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False

        return True

    def isEulerian(self):
        # Check if all non-zero degree vertices are connected
        if not self.isConnected():
            return False

        # Check if all vertices have even degree
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0 or len(self.graph[i]) == 0:
                return False
        return True

    def findEulerianPath(self):
        if not self.isEulerian():
            return None
        graph = self.graph.copy()
        # Create empty stack and list
        stack = []
        path = []
        # Add first vertex to stack
        stack.append(0)
        # Loop until stack is empty
        while len(stack) > 0:
            # Get current vertex
            v = stack[-1]
            # If current vertex has no neighbors, add to path and remove from stack
            if len(graph[v]) == 0:
                path.append(stack.pop())
            # If current vertex has neighbors, add neighbor to stack and remove edge
            else:
                stack.append(graph[v][-1])
                graph[v].pop()
                graph[stack[-1]].remove(v)
        # Return path
        return path

    def __str__(self):
        return str(self.graph)


def generate_graph(n: int, density: float):
    g = Graph(n)

    # Create list of all possible edges
    all_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            all_edges.append((i, j))

    # Randomly select edges
    random.shuffle(all_edges)

    # Add edges to graph
    for i in range(len(all_edges)):
        if random.random() < density:
            g.addEdge(all_edges[i][0], all_edges[i][1])
    return g


def generate_eulerian_graph(n: int, density: float):
    g = generate_graph(n, density)
    while g.isEulerian() == False:
        g = generate_graph(n, density)
    return g

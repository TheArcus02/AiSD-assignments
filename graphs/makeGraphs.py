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

        # Create a copy of the graph
        graph_copy = defaultdict(list)
        for i in self.graph:
            graph_copy[i] = self.graph[i].copy()

        # If both conditions are satisfied, return True
        return True, graph_copy

    def findEulerianPath(self):
        is_eulerian, graph_copy = self.isEulerian()  # type: ignore
        if not is_eulerian:
            return None

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
            if len(graph_copy[v]) == 0:
                path.append(stack.pop())
            # If current vertex has neighbors, add neighbor to stack and remove edge
            else:
                stack.append(graph_copy[v][-1])
                graph_copy[v].pop()
                graph_copy[stack[-1]].remove(v)
        # Return path
        return path

    def findHamiltonCycle(self, all_cycles=False):

        path = []
        path.append(0)

        visited = [False] * self.V
        visited[0] = True

        if not self.hamCycleUtil(path, 1, visited, all_cycles):
            return False
        return True

    def hamCycleUtil(self, path: list[int], pos: int, visited: list[bool], all_cycles: bool):

        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cycle
            if path[0] in self.graph[path[pos-1]]:
                # Include source vertex
                # into the path and
                # * Print all cycles *

                #  path.append(0)

                # for i in range(self.V):
                #     print(path[i], end=" ")
                # print()

                # path.pop()

                return True
            return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in self.graph[path[pos-1]]:

            if self.isSafe(v, pos, path) and not visited[v]:
                path.append(v)
                visited[v] = True

                if self.hamCycleUtil(path, pos+1, visited, all_cycles) and not all_cycles:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                visited[v] = False
                path.pop()
        return False

    def isSafe(self, v, pos, path) -> bool:
        # Check if current vertex and last vertex
        # in path are adjacent
        if v not in self.graph[path[pos-1]]:
            return False

        # Check if current vertex not already in path
        if v in path:
            return False

        return True

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

    # if you want to generate a graph with a Hamilton cycle
    # add: and g.findHamiltonCycle() in perentheses
    while not g.isEulerian():
        g = generate_graph(n, density)
    return g

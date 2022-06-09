# Kruskal's algorithm in Python

# Dict for index to vertex mapping
index_to_vertex = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%s - %s : %d" % (index_to_vertex[u], index_to_vertex[v], weight))


g = Graph(6)
# g.add_edge('A', 'B', 4)
# g.add_edge('A', 'C', 4)
# g.add_edge('B', 'C', 2)
# g.add_edge('C', 'D', 3)
# g.add_edge('C', 'E', 2)
# g.add_edge('C', 'F', 4)
# g.add_edge('D', 'F', 3)
# g.add_edge('E', 'F', 3)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 4, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 5, 3)
g.add_edge(4, 5, 3)

g.kruskal_algo()
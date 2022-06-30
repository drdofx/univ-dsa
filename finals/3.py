# Kruskal's algorithm in Python

# Dict for index to vertex mapping
index_to_vertex = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I'}

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.total_weight = 0

    def get_key(self, val):
        for key, value in index_to_vertex.items():
            if val == value:
                return key
    
        return "key doesn't exist"

    def add_edge(self, u, v, w):
        u_in_index = self.get_key(u)
        v_in_index = self.get_key(v)
        self.graph.append([u_in_index, v_in_index, w])

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
            self.total_weight += weight
            print("%s - %s : %d" % (index_to_vertex[u], index_to_vertex[v], weight))
            
        print("\n" + "Total weight MST yang terbentuk: " + str(self.total_weight))

g = Graph(9)
g.add_edge('A', 'B', 2)
g.add_edge('A', 'G', 3)
g.add_edge('A', 'F', 7)
g.add_edge('B', 'C', 4)
g.add_edge('B', 'G', 6)
g.add_edge('C', 'H', 2)
g.add_edge('C', 'D', 2)
g.add_edge('D', 'H', 8)
g.add_edge('D', 'E', 1)
g.add_edge('E', 'F', 6)
g.add_edge('E', 'I', 2)
g.add_edge('F', 'I', 5)
g.add_edge('G', 'I', 1)
g.add_edge('G', 'H', 3)
g.add_edge('H', 'I', 4)


# g.add_edge(0, 1, 4)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 2, 2)
# g.add_edge(2, 3, 3)
# g.add_edge(2, 4, 2)
# g.add_edge(2, 5, 4)
# g.add_edge(3, 5, 3)
# g.add_edge(4, 5, 3)

g.kruskal_algo()
# Breadth-first search algorithm for graph traversal
# Using Deque (Double ended queue)

from collections import deque

graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]

        remaining_elemnents = set(adj_nodes).difference(visited_vertices)
        if len(remaining_elemnents) > 0:
            for elem in sorted(remaining_elemnents):
                graph_queue.append(elem)
                visited_vertices.append(elem)

    return visited_vertices

print(breadth_first_search(graph, 'A'))

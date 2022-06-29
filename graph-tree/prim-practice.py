# Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
V = 5

# Dict for index to vertex mapping
index_to_vertex = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
# create a 2d array of size 6x6
# for adjacency matrix to represent graph
# G = [[0, 5, 0, 2, 0],
#      [6, 0, 3, 0, 0],
#      [0, 0, 0, 0, 12],
#      [0, 0, 12, 0, 7],
#      [0, 14, 0, 0, 0]]

G = [[0, 5, 0, 4, 0],
     [5, 0, 3, 0, 12],
     [0, 3, 0, 8, 6],
     [4, 0, 8, 0, 3],
     [0, 12, 6, 3, 0]]

# create a array to track selected vertex
# selected will become true otherwise false
# selected = [0, 0, 0, 0, 0, 0]
selected = [False, False, False, False, False]
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# create a variable to store all weight
total_weight = 0
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        # print(index_to_vertex[i], selected[i])
        if selected[i]:
            for j in range(V):
                # print(index_to_vertex[j], selected[j])
                # print(index_to_vertex[i], index_to_vertex[j], (G[i][j]))
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge (value 0 means there is no edge)
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
                        # print(minimum)
    print(index_to_vertex[x] + " - " + index_to_vertex[y] + " : " + str(G[x][y]))
    selected[y] = True
    total_weight += G[x][y]
    no_edge += 1

print(total_weight)
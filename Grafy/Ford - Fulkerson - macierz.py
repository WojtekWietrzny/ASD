from collections import deque


graph = [[0 for j in range(12)] for i in range(12)]
graph[0][1] = 1
graph[0][2] = 1
graph[0][3] = 1
graph[0][4] = 1
graph[0][5] = 1

graph[1][6] = 1
graph[1][7] = 1
graph[1][9] = 1
graph[2][8] = 1
graph[2][10] = 1
graph[3][6] = 1
graph[3][8] = 1
graph[4][9] = 1
graph[5][9] = 1

graph[6][11] = 1
graph[7][11] = 1
graph[8][11] = 1
graph[9][11] = 1
graph[10][11] = 1

print(graph)


M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]

def change_graph(M):
    n = len(M)
    graph = [[0 for i in range(2 * n + 2)] for j in range(2 * n + 2)]
    for i in range(1, n + 1):
        graph[0][i] = 1
    for i in range(n + 1, 2 * n + 1):
        graph[i][2 * n + 1] = 1
    for i in range(n):
        coutner = 0
        for element in M[i]:
            graph[i+1][element+n+1] = 1
    return graph


g = change_graph(M)
print(g)
def Ford_Fulkerson(g, source, sink):
    graph = g
    Max_Flow = 0
    parent = [-1]*len(graph)
    while BFS(graph, source, sink, parent):
        v = sink
        path_flow = float('inf')
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]
        Max_Flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return Max_Flow



def BFS(graph, source, sink, parent):
    visited = [False for i in range(len(graph))]
    queue = deque()
    queue.append(source)
    visited[source] = True
    while len(queue) > 0:
        curr = queue.pop()
        for neighbour in range(len(graph)):
            if visited[neighbour] == False and graph[curr][neighbour] > 0:
                visited[neighbour] = True
                parent[neighbour] = curr
                queue.append(neighbour)

    return visited[sink]

a = Ford_Fulkerson(graph, 0, len(graph)-1)
print(a)
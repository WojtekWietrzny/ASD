from queue import Queue


# BFS listy sąsiedctwa

def BFSLS(G, s):
    V = len(G)
    q = Queue()
    visited = [False for _ in range(V)]
    d = [-1 for _ in range(V)]
    visited[s] = True
    d[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()

        for v, w in G[u]:
            if not visited[v]:
                d[v] = d[u] + w
                visited[v] = True
                q.put(v)

    return max(d)


def zadanie(G):
    V = len(G)
    result = float('inf')
    for u in range(V):
        max_d = BFSLS(G, u)
        if max_d < result:
            result = max_d
            idx = u

    return idx


def undirected_weighted_graph_list(E):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G

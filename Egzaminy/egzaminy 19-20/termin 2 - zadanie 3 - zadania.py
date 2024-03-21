
def create_graph(T):
    n = len(T)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 1:
                G[i].append(j)
            elif T[i][j] == 2:
                G[j].append(i)
    return G

def topological_sort(G: 'graph represented using adjacency lists'):
    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result

def tasks(T):
    G = create_graph(T)
    return topological_sort(G)
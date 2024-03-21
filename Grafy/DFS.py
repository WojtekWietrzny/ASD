"""
implementacja DFS
"""


def DFS(G):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    times = [float('inf') for v in range(n)]
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        time += 1
        visited[u] = True
        times[u] = time
        for v in G[u]:
            if not visited[u]:
                parent[v] = u
                DFSVisit(G, v)
        """print(time)
        time += 1"""

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    #print(time)
    return times


G = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]

print(DFS(G))

"""
implementacja BFS - Breadth-Fisrt Search
"""
from collections import deque

def BFS(G,s):
    #G = (V,E), s należy do grafu
    Q = deque()
    n = len(G)
    d = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    Q.append(s)
    visited[s] = True
    d[s] = 0
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u]+1
                parent[v] = u
                Q.append(v)
    return d


G = [[1,2,3],[0,2],[0,1,4],[0,4],[2,3]]
print(BFS(G,0))
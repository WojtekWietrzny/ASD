"""
zadanie:

"""

"""
implementacja BFS - Breadth-Fisrt Search
"""
from collections import deque



def longer(G,s,t):
    n = len(G)
    d = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]

    def BFS(G, s, t, version):
        # G = (V,E), s należy do grafu
        n = len(G)
        nonlocal d
        nonlocal visited
        nonlocal parent
        if version == 1:
            d = [-1 for v in range(n)]
            visited = [False for v in range(n)]
            parent = [None for v in range(n)]
        Q = deque()
        Q.append(s)
        visited[s] = True
        d[s] = 0
        while len(Q) > 0:
            current = Q.popleft()
            if current == t:
                break
            for v in G[current]:
                if not visited[v]:
                    visited[v] = True
                    d[v] = d[current] + 1
                    parent[v] = current
                    Q.append(v)
        return d[t]

    shortest_distance = BFS(G,s,t,0)
    if shortest_distance == 0:
        return None
    current  = t
    current_parent = parent[t]
    while current != s:
        G[current].remove(current_parent)
        G[current_parent].remove(current)
        if BFS(G,s,t,1) > shortest_distance or d[t] == 0:
            return(current_parent, current)
        else:
            G[current].append(current_parent)
            G[current_parent].append(current)
            current = current_parent
            current_parent = parent[current_parent]
        return None



G = [[1,4],[0,2],[1,3],[2,5],[0,5],[4,3]]
print(longer(G,0,2))


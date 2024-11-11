"""
implementacja BFS - Breadth-Fisrt Search
"""
from collections import deque

def BFS(G:'graph using adjacency list',s:'start vertice'):
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
    return d,parent


G_lecture = [[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
G = [[1,2,3],[0,2],[0,1,4],[0,4],[2,3]]
print(BFS(G_lecture,0))

def getPath(G:'graph using adjacency list',s:'start vertice',e:'end vertice'):
    distance,parents = BFS(G,e)
    print(parents)
    path=[]
    parent = parents[s]
    path.append(s) #if we want to include the starting vertice in a path
    while parent != None:
        path.append(parent)
        parent = parents[parent]

    return path

print(getPath(G_lecture,0,4))






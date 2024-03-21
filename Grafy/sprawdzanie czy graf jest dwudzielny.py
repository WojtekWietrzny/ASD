"""
zadanie:
sprawdzić czy graf (nieskierowany) jest dwudzielny
pomysł:
trzeba najpierw sprawdzić czy graf jest spójny
dla każdej spójnej sprawdzamy to co na dole
BFS + kolorujemy wierzchołki na przeciwny niż ten który ma wierzchołek z którego przyszliśmy
"""
from collections import deque

def isBipartite(G,s):
    n=len(G)
    colors=[0 for i in range(n)]

    Q=deque()

    Q.append(s)
    colors[s]=1

    while len(Q)>0:
        u=Q.popleft()

        for v in G[u]:
            if colors[v]==0:
                colors[v]=-1*colors[u]
                Q.append(v)

            elif colors[u]==colors[v]:
                return False

    return True

G=[[1,2],[0],[0,3,4,5],[2],[2],[2]]
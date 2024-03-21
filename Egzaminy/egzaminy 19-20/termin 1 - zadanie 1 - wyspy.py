"""
idea:
można zrobić z tego graf
wierzchołki - wyspy
krawędzie - połączenia komunikacyjne między wyspami
waga krawędzi to koszt podróży danym środkiem transportu
potem potrzeba jakąś flagę i puszczamy po tym Dijkstre
z jakąś flagą, trzeba pamiętać jak doszedłeś do danego pola
"""

"""
idea z potrojonym grafem
tworzysz potrojony graf - robisz dla każdego wierzchołka jego wersja typu "doszedłem do niego poprzez"
-prom
-samolot
-most
i dla np. opcji prom usuwasz wierzchołki wychodzących z niego promów etc.
"""

"""
sposób z BFS-em
pierwszy wykład z grafów ważonych

"""

from queue import PriorityQueue

def dijkstra(G, s):
    V = len(G)
    d = [float('inf') for _ in range(V)]
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    d[s] = 0

    q = PriorityQueue()

    q.put([0, s, None])

    def relax(u, v, w):

        if d[v] > d[u] + w:
            d[v] = d[u] + w
            parent[v] = u

        return d[v]

    while not q.empty():

        dist, u, last = q.get()

        if not visited[u]:
            visited[u] = True

            for v in range(V):
                w = G[u][v]
                if w != last and w != 0:
                    l = relax(u, v, w)
                    q.put([l, v, w])
    return d


def islands(G, a, b):
    d = dijkstra(G, a)

    return d[b]
"""
idea:
robimy dijkstre z flagą, żeby znaleźć najkrótszą ściężkę długości 3
"""

from queue import PriorityQueue
from math import inf

def dijkstra(G,D,L):
    n=len(G)
    distance = [[inf]*3 for _ in range(n)]
    Q = PriorityQueue()
    for i in range(3):
        distance[D][i] = 0

    Q.put((0, D, 3))
    while not Q.empty():
        w1, u, ilosc = Q.get()
        for v, w2 in G[u]:
            if ilosc > 0 and v != L:
                if distance[v][ilosc - 1] > w1 + w2:
                    distance[v][ilosc - 1] = w1 + w2
                    Q.put((distance[v][ilosc - 1], v, ilosc - 1))

            elif ilosc == 0 and v == L:
                distance[L][0] = min(distance[L][0], w1 + w2)
    return distance[L]


def turysta(G, D, L):
    n=-1
    for v, u, w in G:
        n = max(n, u, v)
    H = [[]for _ in range(n + 1)]
    for v, u, w in G:
        H[v].append((u, w))
        H[u].append((v, w))

    result = dijkstra(H,D,L)
    return result[0]

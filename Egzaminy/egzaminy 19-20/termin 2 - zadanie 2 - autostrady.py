from queue import PriorityQueue
from math import sqrt


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent)

    return x.parent


def union(x, y):
    x = findset(x)
    y = findset(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y

        if x.rank == y.rank:
            y.rank += 1


def connected(x, y):
    if findset(x) == findset(y):
        return True

    return False


def kruskal(E, n):
    T = []
    Z = []
    cnt = 0

    for i in range(n):
        Z.append(Node(i))

    q = PriorityQueue()
    for e in E:
        q.put([e[0], e[1], e[2]])

    while not q.empty():
        u = q.get()

        if cnt == n - 1:
            break

        if findset(Z[u[1]]) != findset(Z[u[2]]):
            union(Z[u[1]], Z[u[2]])
            T.append(u)
            cnt += 1

    if cnt != n - 1:
        return None

    for i in range(1, len(T)):
        if findset(Z[T[i][1]]) != findset(Z[T[0][1]]) or findset(Z[T[i][2]]) != findset(Z[T[0][2]]):
            return None

    return T


def odleglosc(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def krawedzie(M):
    E = []
    V = len(M)
    for i in range(V):
        for j in range(i + 1, V):
            E.append((odleglosc(M[i], M[j]), i, j))

    return E


def zadanie(M):
    n = len(M)
    E = krawedzie(M)

    E.sort(reverse=True, key=lambda e: e[0])

    min_diff = float('inf')
    while len(E) >= n - 1:

        T = kruskal(E, n)
        if T is not None:
            max_edge = T[-1][0]
            min_edge = E.pop()
            min_edge = min_edge[0]
            min_diff = min(min_diff, max_edge - min_edge)
            print(max_edge, min_edge)
        else:
            break

    return min_diff
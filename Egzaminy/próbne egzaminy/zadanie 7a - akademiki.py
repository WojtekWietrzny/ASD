"""
idea:
wierzchołki to ludzie
wierzchołki to pokoje
krawędzie między ludźmi a preferencjami
puszczasz max matching
to da nam złożoność V * E, czyli n * 3n, czyli O(n^2)
"""


def akademik(T):
    n = len(T)
    G = [[] for _ in range(n)]

    pustych = 0
    for i in range(n):
        if T[i] == (None, None, None):
            pustych += 1
    for i in range(n):
        for j in range(3):
            if T[i][j] == None:
                continue
            G[i].append(T[i][j])
    print(G)
    adjacents = [[] for _ in range(n + 1)]
    pair_U = [0 for _ in range(n + 1)]
    pair_V = [0 for _ in range(n + 1)]
    distance = [0 for _ in range(n + 1)]

    for i in range(n):
        for element in G[i]:
            adjacents[i].append(element)
    G.append([])

    def bfs():
        Q = deque()
        distance[0] = float('inf')
        for u in range(1, n + 1):
            if pair_U[u] == 0:
                distance[u] = 0
                Q.append(u)
            else:
                distance[u] = float('inf')
        while len(Q) != 0:
            u = Q.pop()
            if distance[u] < distance[0]:
                for v in G[u]:
                    if distance[pair_V[v]] == float('inf'):
                        distance[pair_V[v]] = distance[u] + 1
                        Q.append(pair_V[v])
        return distance[0] != float('inf')

    def dfs(u):
        if u != 0:
            for v in adjacents[u]:
                if distance[u] + 1 == distance[pair_V[v]]:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True
            distance[u] = float('inf')
            return False
        return True

    def max_association():
        result = 0
        while bfs():
            for u in range(1, n + 1):
                if pair_U[u] == 0 and dfs(u):
                    result += 1
        return result

    return len(T) - pustych - max_association()


def binworker(M):
    n = len(M)
    adjacents = [[] for _ in range(n + 1)]
    pair_U = [0 for _ in range(n + 1)]
    pair_V = [0 for _ in range(n + 1)]
    distance = [0 for _ in range(n + 1)]

    for i in range(n):
        for element in M[i]:
            adjacents[i].append(element)
    M.append([])

    def bfs():
        Q = deque()
        distance[0] = float('inf')
        for u in range(1, n + 1):
            if pair_U[u] == 0:
                distance[u] = 0
                Q.append(u)
            else:
                distance[u] = float('inf')
        while len(Q) != 0:
            u = Q.pop()
            if distance[u] < distance[0]:
                for v in M[u]:
                    if distance[pair_V[v]] == float('inf'):
                        distance[pair_V[v]] = distance[u] + 1
                        Q.append(pair_V[v])
        return distance[0] != float('inf')

    def dfs(u):
        if u != 0:
            for v in adjacents[u]:
                if distance[u] + 1 == distance[pair_V[v]]:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True
            distance[u] = float('inf')
            return False
        return True

    def max_association():
        result = 0
        while bfs():
            for u in range(1, n + 1):
                if pair_U[u] == 0 and dfs(u):
                    result += 1
        return result

    return max_association()


# wersja szymona 10/10 - 0.16 sekundy

from math import inf

def dfs_visit(G, GD, V, P, i):
    V[i] = True
    for nb in G[i]:
        idd = str(i) + "_" + str(nb)
        if not V[nb] and GD[idd] != 0:
            P[nb] = i
            dfs_visit(G, GD, V, P, nb)

def dfs(G, GD, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, GD, V, P, s)
    return V[t]


def ford_fulkerson(G, s, t):
    GD = {}
    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(u) + "_" + str(G[u][v])
            iddBack = str(G[u][v]) + "_" + str(u)
            GD[idd] = 1
            if GD.get(iddBack) == None:
                GD[iddBack] = 0
    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(G[u][v]) + "_" + str(u)
            if GD[idd] == 0:
                G[G[u][v]].append(u)
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, GD, s, t, P):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, GD[str(P[current]) + "_" + str(current)])
            current = P[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = P[v]
            GD[str(u) + "_" + str(v)] -= current_flow
            GD[str(v) + "_" + str(u)] += current_flow
            v = P[v]
    return max_flow


def akademik(T):
    s = len(T) * 2
    t = s + 1
    n = t + 1
    n1 = len(T)

    G = [[] for _ in range(n)]
    for i in range(len(T)):
        for j in range(3):
            if T[i][j] != None:
                G[i].append(n1 + T[i][j])
    for i in range(len(T)):
        G[s].append(i)
        G[n1 + i].append(t)

    pustych = 0
    for i in range(len(T)):
        if T[i] == (None, None, None):
            pustych += 1

    return len(T) - pustych - ford_fulkerson(G, s, t)




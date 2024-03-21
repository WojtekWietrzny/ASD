"""
idea:
wrzucamy połączenia na graf, szukamy punktów artykulacji
ta idea daje wzorcówkę
"""

time = 0

def koleje(B):
    time = 0
    def dfs(G, ART, LOW, D, P, v):
        nonlocal time
        children = 0

        time += 1
        LOW[v] = time
        D[v] = time

        for s in G[v]:
            if D[s] is None:
                children += 1
                dfs(G, ART, LOW, D, P, s)

                if LOW[s] >= D[v]:
                    ART[v] = True
                LOW[v] = min(LOW[v], LOW[s])
            else:
                LOW[v] = min(LOW[v], D[s])
        return children

    def articulation(G):
        # czas odwiedzenia
        nonlocal time

        n = len(G)
        # tablica pamiętająca czy wierzchołek jest punktem artykulacji
        ART = [False for _ in range(n)]
        # LOW z wykładu
        LOW = [None for _ in range(n)]
        # czas odwiedzenia D(iscorvery time)
        D = [None for _ in range(n)]
        # tablica parentów
        P = [None for _ in range(n)]

        for i in range(n):
            if D[i] is None:
                if dfs(G, ART, LOW, D, P, i) > 1:
                    ART[i] = True
                else:
                    ART[i] = False

        points = 0
        for i in range(n):
            if ART[i] == True:
                points += 1
        return points


    for i in range(len(B)):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1], B[i][0])
    B.sort(key = lambda x:(x[0], x[1]))
    n = 0
    for elem in B:
        n = max(n,elem[1])
    n += 1
    G = [[] for _ in range(n)]
    last = None

    for i in range(len(B)):
        if last != B[i]:
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])
    return articulation(G)

B = [(3, 1), (0, 1), (4, 2), (1, 2), (0, 1), (2, 4), (2, 4), (0, 3), (2, 4), (1, 0), (2, 1)]

print(koleje(B))
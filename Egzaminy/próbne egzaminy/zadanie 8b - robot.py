#złożoność n^3
def floydwar(G):
    inf = float('inf')
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = inf
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G

def robot(G, P):
    n = len(G)
    G2 = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for nb in G[i]:
            G2[i][nb[0]] = nb[1]
            G2[nb[0]][i] = nb[1]
    floydwar(G2)

    sum = 0
    current = P[0]
    for i in range(1, len(P)):
        sum += G2[current][P[i]]
        current = P[i]
    return sum

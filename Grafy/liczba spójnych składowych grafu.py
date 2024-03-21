"""
zadanie:
policzyć liczbę spójnych składowych grafu (nieskierowanego)
pomysł:
uruchamiamy DFS - każde przejście jego pętli zewnętrznej for będzie zliczane - to jest liczba spójnych składowych
każde przejście takiej pętli to jedna spójna składowa w grafie
po przejściu wchodzimy w inny wierzchołek, który jeszcze nie był odwiedzony
"""
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    counter = 0
    def DFS_visit(G,u):
        nonlocal visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G,v)
    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)
            counter += 1
    return counter

G = [
    [1],
    [0,2],
    [1],
    []]

print(DFS(G))
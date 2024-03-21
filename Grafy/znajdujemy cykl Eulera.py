"""
zadanie:
znajdujemy ścieżkę Eulera
reprezentacja grafu macierzowa

pomysł:
ten z wykładu - DFS, pamiętamy które już przeszliśmy

implementacja:
z usuwaniem krawędzi
"""

def dfs_visit(v,M,result):
    n = len(M)
    for i in range(n):
        if M[v][i] == True:
            M[v][i] = False
            M[i][v] = False
            dfs_visit(i, M, result)
    result.append(v)


def euler_cycle(M):
    M = [M[i][:] for i in range(len(M))]
    result = []
    dfs_visit(0,M,result)
    return result
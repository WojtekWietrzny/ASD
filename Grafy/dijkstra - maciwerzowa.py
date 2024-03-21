
def dijkstra(M, s):
    n = len(M)
    dist = [float("inf") for _ in range (n)]
    visited = [False for _ in range(n)]
    dist[s] = 0
    parent = [None for _ in range(n)]
    while True:
        min_dist, index = float("inf"), -1
        for i in range(n):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                index = i
        if index == -1:
            return dist, parent
        visited[index] = True



# normalnie jest E log V złożoność, dla skierowanego acyklicznego innym podejściem można osiągnąć złożoność E - w grafie rzadkim wszystko

"""
algorymt na tą złożoność O(E)
sortujemy rgaf topologicznie 
wykonujemy relaksacje dla wszystkich z danej grupy, a potem przechodzimy do kolejnej grupy
bierzemy wierzchołek startowy, nie sprawdzamy wierzchołków 
co dalej to bóg jeden wie


"""
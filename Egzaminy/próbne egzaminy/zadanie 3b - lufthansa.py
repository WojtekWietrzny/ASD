"""
idea:
MST - kruskal albo Prim
zmieniamy krawędzie wag na takie z minusem, żeby największe drzewo rozpinające,
było tak naprawdę najmniejsze w tym pierwotnym
"""

from queue import PriorityQueue

def lufthansa ( G ):
    n = len(G)
    whole_sum = 0
    for i in range(n):
        for j in range(len(G[i])):
            whole_sum += G[i][j][1]
    whole_sum /= 2

    G_new = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            G_new[i][j].append = ((G[i][j][0], -G[i][j][1]))

    """def is_consistent(G: 'graph represented using adjacency lists'):
        n = len(G)
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v, _ in G[u]:
                if visited[v]:
                    dfs(v)

        dfs(0)
        return all(visited)"""

    def prims(G: 'graph represented by adjacency lists'):
        """if not is_consistent(G):
            return [], []"""
        n = len(G)
        inf = float('inf')
        parents = [-1] * n
        weights = [inf] * n
        processed = [False] * n
        pq = PriorityQueue()
        pq.put((0, 0))

        while not pq.empty():
            u_weight, u = pq.get()
            # Skip a vertex if it was processed before
            if processed[u]: continue
            # If we remove the vertex from a priority queue this must be a vertex
            # with the lowest weight in a queue so we will mark this vertex as
            # processed because all the future occurrences of this vertex
            # in a priority queue must be skipped
            processed[u] = True
            # Loop over all the u vertex's neighbours and update parents of such
            # vertices which are not processed and their current weight is greater
            # than the u_weight
            for v, e_weight in G[u]:
                if not processed[v] and e_weight > weights[v]:
                    parents[v] = u
                    weights[v] = e_weight
                    pq.put((e_weight, v))
        return parents, weights

    def get_MST(G: 'graph represented by adjacency lists') -> 'minimum spanning tree graph':
        parents, weights = prims(G)
        n = len(G)
        G = [[] for _ in range(n)]
        sum = 0
        for u in range(n):
            if parents[u] >= 0:
                G[parents[u]].append((u, weights[u]))
                G[u].append((parents[u], weights[u]))
                sum += weights[u]
        return sum

    sum = - get(MST)
    return whole_sum - sum

# czemu nie działa?

G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ]
]

print(lufthansa(G))
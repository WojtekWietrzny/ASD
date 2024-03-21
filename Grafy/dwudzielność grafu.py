def is_bipartite(G: 'graph represented using adjacency lists') -> bool:
    n = len(G)
    colors = [0] * n  # 0 means no color (we will use 2 colors as we want to check if it's bipartite)

    def dfs(u):
        for v in G[u]:
            if not colors[v]:
                colors[v] = -1 * colors[u]
                if not dfs(v): return False
            elif colors[v] == colors[u]:
                return False
        return True

    for u in range(n):
        if not colors[u]:
            colors[u] = 1
            if not dfs(u): return False

    return True


graph = [[3,4,5,6],[3,4,5,6],[3,4,5,6],[0,1,2],[0,1,2],[0,1,2],[0,1,2]]
graph_2 = [[1,4],[0,2],[1,3],[2,4],[1,4]]
graph_3 = [[1],[0,2],[1,3],[2,4],[3]]
print(is_bipartite(graph))
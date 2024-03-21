# Python3 implementation of Hopcroft Karp algorithm for
# maximum matching
from queue import Queue
from collections import deque

INF = 2147483647
NIL = 0


# A class to represent Bipartite graph for Hopcroft
# 3 Karp implementation
class BipGraph(object):
    # Constructor
    def __init__(self, m, n):
        # m and n are number of vertices on left
        # and right sides of Bipartite Graph
        self.__m = m
        self.__n = n
        # adj[u] stores adjacents of left side
        # vertex 'u'. The value of u ranges from 1 to m.
        # 0 is used for dummy vertex
        self.__adj = [[] for _ in range(m + 1)]

    # To add edge from u to v and v to u
    def addEdge(self, u, v):
        self.__adj[u].append(v)  # Add u to v’s list.

    # Returns true if there is an augmenting path, else returns
    # false
    def bfs(self):
        Q = Queue()
        # First layer of vertices (set distance as 0)
        for u in range(1, self.__m + 1):
            # If this is a free vertex, add it to queue
            if self.__pairU[u] == NIL:
                # u is not matched3
                self.__dist[u] = 0
                Q.put(u)
            # Else set distance as infinite so that this vertex
            # is considered next time
            else:
                self.__dist[u] = INF
        # Initialize distance to NIL as infinite
        self.__dist[NIL] = INF
        # Q is going to contain vertices of left side only.
        while not Q.empty():
            # Dequeue a vertex
            u = Q.get()
            # If this node is not NIL and can provide a shorter path to NIL
            if self.__dist[u] < self.__dist[NIL]:
                # Get all adjacent vertices of the dequeued vertex u
                for v in self.__adj[u]:
                    #  If pair of v is not considered so far
                    # (v, pairV[V]) is not yet explored edge.
                    if self.__dist[self.__pairV[v]] == INF:
                        # Consider the pair and add it to queue
                        self.__dist[self.__pairV[v]] = self.__dist[u] + 1
                        Q.put(self.__pairV[v])
        # If we could come back to NIL using alternating path of distinct
        # vertices then there is an augmenting path
        return self.__dist[NIL] != INF

    # Returns true if there is an augmenting path beginning with free vertex u
    def dfs(self, u):
        if u != NIL:
            # Get all adjacent vertices of the dequeued vertex u
            for v in self.__adj[u]:
                if self.__dist[self.__pairV[v]] == self.__dist[u] + 1:
                    # If dfs for pair of v also returns true
                    if self.dfs(self.__pairV[v]):
                        self.__pairV[v] = u
                        self.__pairU[u] = v
                        return True
            # If there is no augmenting path beginning with u.
            self.__dist[u] = INF
            return False
        return True

    def hopcroftKarp(self):
        # pairU[u] stores pair of u in matching where u
        # is a vertex on left side of Bipartite Graph.
        # If u doesn't have any pair, then pairU[u] is NIL
        self.__pairU = [0 for _ in range(self.__m + 1)]

        # pairV[v] stores pair of v in matching. If v
        # doesn't have any pair, then pairU[v] is NIL
        self.__pairV = [0 for _ in range(self.__n + 1)]

        # dist[u] stores distance of left side vertices
        # dist[u] is one more than dist[u'] if u is next
        # to u'in augmenting path
        self.__dist = [0 for _ in range(self.__m + 1)]
        # Initialize result
        result = 0

        # Keep updating the result while there is an
        # augmenting path.
        while self.bfs():
            # Find a free vertex
            for u in range(1, self.__m + 1):
                # If current vertex is free and there is
                # an augmenting path from current vertex
                if self.__pairU[u] == NIL and self.dfs(u):
                    result += 1
        return result


# Driver Program
if __name__ == "__main__":
    g = BipGraph(4, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.addEdge(4, 4)
    print("Size of maximum matching is %d" % g.hopcroftKarp())


def BFS(G,s):
    #G = (V,E), s należy do grafu
    Q = deque()
    n = len(G)
    d = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    Q.append(s)
    visited[s] = True
    d[s] = 0
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u]+1
                parent[v] = u
                Q.append(v)
    return d

def DFS(G):
    n = len(G)
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        nonlocal visited
        nonlocal parent
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[u]:
                parent[v] = u
                DFSVisit(G, v)
        time += 1

    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u)
    print(time)

# mój kod








M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]

from queue import Queue

def change_graph(M):
    n = len(M) # długość listy reprezentującej graf z samymi pracownikami
    for i in range(n):
        M.append([])
    for i in range(n):
        for element in M[i]:
            M[element+n].append(i)
    m = len(M) # długość listy reprezentujacej graf po dodaniu maszyn
    return M
G = change_graph(M)
def colorize_vertices(G):
    n = len(G)

    # 0 means no color (we will use 2 colors as we want to divide vertices
    # into two disjoint sets)
    colors = [0] * n

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
            if not dfs(u): return []  # Return an empty list if a graph is not bipartite

    return colors


def add_source_and_sink(G, colors):
    n = len(G)
    m = len(colors)

    # Add a source and a sink
    G.append([])
    G.append([])

    for u in range(m):
        # Add outgoing edges from a source to all vertices of a color 1
        if colors[u] == 1:
            G[n].append((u, 1))
        # Add ingoing edges to the sing from all vertices of a color -1
        else:
            G[u].append((n + 1, 1))


def map_graph(G: 'graph represented by adjacency lists'):
    n = len(G)
    G2 = [[] for _ in range(n)]
    w = n

    for u in range(n):
        for v in G[u]:
            if u < v:
                G2.append([])
                G2[u].append((w, 1))
                G2[w].append((v, 1))
                w += 1
            else:
                G2[u].append((v, 1))

    return G2


def add_back_edges(G):
    n = len(G)
    counts = [0] * n  # Numbers of edges in an initial graph (before modification)

    for u in range(n):
        counts[u] = len(G[u])

    for u in range(n):
        for i in range(counts[u]):
            v = G[u][i][0]
            G[v].append((u, 0))  # Add an edge with no weight


def update_flow(flow, parents, t):
    u = t

    while parents[u] is not None:
        v = parents[u]
        flow[v][u] += 1
        flow[u][v] -= 1
        u = v


def edmonds_karp(G: 'graph represented by adjacency lists',
                 s: 'source vertex',
                 t: 'target vertex'):
    n = len(G)
    inf = float('inf')
    flow = [[0] * n for _ in range(n)]
    parents = [None] * n
    visited = [0] * n
    token = 1  # Number of iteration to check which vertices have been visited

    while True:
        q = Queue()
        q.put(s)
        visited[s] = token
        found_path = False

        while not q.empty():
            u = q.get()

            if u == t:
                update_flow(flow, parents, t)
                found_path = True
                break

            for v, capacity in G[u]:
                remaining = capacity - flow[u][v]
                if visited[v] != token and remaining > 0:
                    visited[v] = token
                    parents[v] = u
                    q.put(v)

        if not found_path: break
        token += 1

    return token - 1


def maximum_association(G: 'undirected graph represented by adjacency lists'):
    colors = colorize_vertices(G)
    # If a graph is not bipartite, return -1
    if not colors: return -1
    G2 = map_graph(G)
    n = len(G2)
    add_back_edges(G2)
    add_source_and_sink(G2, colors)
    return edmonds_karp(G2, n, n + 1)


"""
podejście Fordem Fulkersonem
"""


def map_graph(G: 'graph represented by adjacency lists'):
    n = len(G)
    for i in range(n):
        G.append([])
    G.append([] * n)
    w = n

    for u in range(n):
        for v, weight in G[u]:
            if u < v:
                G2.append([])
                G2[u].append((w, weight))
                G2[w].append((v, weight))
                w += 1
            else:
                G2[u].append((v, weight))

    return G2


""" Koniec zmian """


def add_back_edges(G):
    n = len(G)
    counts = [0] * n  # Numbers of edges in an initial graph (before modification)

    for u in range(n):
        counts[u] = len(G[u])

    for u in range(n):
        for i in range(counts[u]):
            v = G[u][i][0]
            G[v].append((u, 0))  # Add an edge with no weight


def ford_fulkerson(G: 'graph represented by adjacency lists', s: 'source vertex', t: 'target vertex'):
    # Create a directed graph from the input graph
    G = map_graph(G)

    n = len(G)
    inf = float('inf')
    flow = [[0] * n for _ in range(n)]
    visited = [0] * n
    token = 1  # Number of iteration to check which vertices have been visited
    max_flow = 0

    add_back_edges(G)

    def dfs(u, bottleneck):
        visited[u] = token

        if u == t: return bottleneck

        for v, capacity in G[u]:
            remaining = capacity - flow[u][v]
            if visited[v] != token and remaining > 0:
                new_bottleneck = dfs(v, min(remaining, bottleneck))
                if new_bottleneck:
                    flow[u][v] += new_bottleneck
                    flow[v][u] -= new_bottleneck
                    return new_bottleneck
        return 0

    while True:
        increase = dfs(s, inf)
        if not increase: break
        max_flow += increase
        token += 1

    return max_flow
import heapq
from queue import PriorityQueue

"""def spacetravel( n, E, S, a, b ):
    length = len(E)
    G = [[] for _ in range(n)]
    for i in range(length):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    length_S = len(S)
    for element in S:
        for j in range(length_S):
            if element != S[j]:
                G[element].append((S[j], 0))
    print(G)
    return G



"""
"""def calculate_distances(graph, starting_vertex):
    distances = [float('inf') for vertex in graph]
    distances[starting_vertex] = 0

    pq = [(starting_vertex,0)]
    while len(pq) > 0:
        current_vertex, current_distance = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

                # Only consider this new path if it's better than any path we've
                # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances"""

"""def relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ ):
    if distance[neighbour_num] > distance[node] + node_to_neigh:
        distance[neighbour_num] = distance[node] + node_to_neigh
        PriorQ.put((distance[neighbour_num], neighbour_num))

def Dijkstra(G, s, b):
    distance = [float('inf') for j in range(len(G))]
    distance[s] = 0
    PriorQ = PriorityQueue()
    PriorQ.put((0, s))
    while PriorQ.qsize() > 0:
        curr = PriorQ.get()
        node = curr[1]
        if node == b:
            break
        for neighbour in (G[node]):
            node_to_neigh = neighbour[1]
            neighbour_num = neighbour[0]
            relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ)
    return distance"""

def spacetravel(n, E, S, a, b):
    length = len(E)
    G = [[] for _ in range(n + 1)]
    for i in range(length):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))
    length_S = len(S)
    for i in range(length_S):
        G[n].append((S[i], 0))
        G[i].append((n, 0))
        """for j in range(length_S):
                if element != S[j]:
                    G[element].append((S[j], 0))"""

    def shortest_path(G, start, destination):
        length_G = len(G) + 1
        P_Queue = PriorityQueue()
        dist = [float('inf') for _ in range(length_G + 1)]
        dist[start] = 0
        P_Queue.put((dist[start], start))
        while not P_Queue.empty():
            current = P_Queue.get()
            planet = current[1]
            if planet == destination:
                break
            for planet_neighbour in (G[planet]):
                vertice = planet_neighbour[0]
                weight = planet_neighbour[1]
                if dist[planet] + weight < dist[vertice]:
                    dist[vertice] = dist[planet] + weight
                    P_Queue.put((dist[vertice], vertice))
            if dist[destination] == float('inf'):
                dist[destination] = None
            return dist[destination]

        return shortest_path(G, a, b)
E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
S = [0, 2, 3]
#spacetravel(7, E, S, 1, 5)
#print(calculate_distances(spacetravel(7,E,S, 1, 5),1))
print(spacetravel(7, E, S, 1, 5))

"""Test 0
n=7
E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
S=[0, 2, 3]
a=1
b=5
Poprawny wynik  :  13"""



from zad5testy import runtests
from queue import PriorityQueue

"""
Wojciech Wietrzny 415792 
Opis Algorytmu:
zaczynam od przepisania grafu do reprezentacji listowej, na początek przepisuje same dane wejściowe - krawędzie z listy E
dodatkowo tworzę jeden wierzchołek na końcu, który będzie służył jako łącznik między punktami opisanymi w liście S
do reprezentacji grafu na indeksy poszczególnych planet z listy S dopisuje odnośnik do łącznika, a w łączniku
tworzę krawędzie do wszystkich planet opisanych w liście S
następnie wykorzystuje algorytm Dijkstry podany na wykładzie, żeby znaleźć najkrószą ścieżkę między dwoma planetami
algorytm ten kończe kiedy dojdę do planety destination, wtedy zwracam dystans potrzebny do odbycia podróży na podaną planętę, 
bądź None, jeśli trasa nie istnieje
złożoność oblcizeniowa:
O(S + E + Elog V), czyli efektywnie O(Elog V)
"""

def spacetravel( n, E, S, a, b ):
    length = len(E)
    G = [[] for _ in range(n+1)]
    for i in range(length):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    length_S = len(S)
    for i in range(length_S):
        G[n].append((S[i], 0))
        G[S[i]].append((n, 0))
    def shortest_path(G, start, destination):
        length_G = len(G)
        P_Queue = PriorityQueue()
        dist = [float('inf') for _ in range(length_G)]
        dist[start] = 0
        P_Queue.put((dist[start], start))
        while not P_Queue.empty():
            current = P_Queue.get()
            planet = current[1]
            if planet == destination:
                break
            for planet_neighbour in (G[planet]):
                vertice = planet_neighbour[0]
                weight = planet_neighbour[1]
                if dist[planet] + weight < dist[vertice]:
                    dist[vertice] = dist[planet] + weight
                    P_Queue.put((dist[vertice], vertice))
        if dist[destination] == float('inf'):
            dist[destination] = None
        return dist[destination]
    return shortest_path(G,a,b)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )
from egz1Atesty import runtests

"""
WOJCIECH WIETRZNY 415792
opis algorytmu:
używam algorytmu Dijkstry do obliczenia najkrótszej ścieżki w grafie ważonym między wierzchołkami np. i, a j
problem z zadania dzielę na 2 podproblemy
dla każdego wierzchołka rozważam sytuacje w której on jest tym zamkiem, z którego chcielibyśmy wziąć złoto
wtedy szukam najkrótszej ścieżki do danego zamku, po której przechodzę normalnie
następnie wywołuje Dijkstre w trybie wanted, czyli do wagę każdej krawędzi po której się poruszam, podwajam, oraz dodaje do niej r
czyli efektywnie szukam najkrótszej ścieżki do każdego zamku z którego potencjalnie mogę chcieć wziąć złoto
następnie szukam najkrószej ścieżki z tego zamku do końca, rozważając że jestem już po wzięciu złota z zamku poszukiwany 
złożoność czasowa:
O(V*ElogV), E ~= V^2, więć ostatecznie O(v^3)
złożoność pamięciowa:
O(V)
"""

"""
WOJCIECH WIETRZNY 415792
opis algorytmu:
używam algorytmu Dijkstry do obliczenia najkrótszych ścieżek z punktu startowego s do każdego pozostałego wierzchołka
następnie używam algorytmu Dijkstry w trybie wanted, w którym koszt każdej ścieżki jest zwiększony dwukrotnie i dodatkowo o r
używam tego algorytmu od ostatniego wierzchołka, tego do którego chcemy dojść, żeby obliczać dla każego wierzchołka koszt
drogi do końca, w przypadku zrabowania pewnego zamku
wynikiem każdego zamku jest koszt ścieżki do niego i koszt ścieżki z dijkstry_wanted pomniejszony o ilość złota w tym zamku
złożoność czasowa:
O(V^2)
złożoność pamięciowa:
O(V)
"""




from queue import PriorityQueue



#złożoność wzorcowa: (błędny minimalnie wynik w ostatnim, czemu?)
def Dijkstra(G,s,t):
    lenght_G = len(G)+ 1
    P_Queue = PriorityQueue()
    dist = [ float('inf') for _ in range(lenght_G + 1)]
    dist[s] = 0
    P_Queue.put((dist[s],s))
    while not P_Queue.empty():
        node = P_Queue.get()
        current_node = node[1]
        if current_node == t:
            break
        for neighbour in (G[current_node]):
            vertice = neighbour[0]
            weight = neighbour[1]
            if dist[current_node] + weight < dist[vertice]:
                dist[vertice] = dist[current_node] + weight
                P_Queue.put((dist[vertice],vertice))
    return dist

def Dijkstra_wanted(G,s,t,r):
    lenght_G = len(G) + 1
    P_Queue = PriorityQueue()
    dist = [float('inf') for _ in range(lenght_G + 1)]
    dist[s] = 0
    P_Queue.put((dist[s], s))
    while not P_Queue.empty():
        node = P_Queue.get()
        current_node = node[1]
        if current_node == t:
            break
        for neighbour in (G[current_node]):
            vertice = neighbour[0]
            weight = 2 * neighbour[1] + r
            if dist[current_node] + weight < dist[vertice]:
                dist[vertice] = dist[current_node] + weight
                P_Queue.put((dist[vertice], vertice))
    return dist

def gold( G,V,s,t,r ):
    mini = float('inf')
    n = len(G)
    result_dijkstra = Dijkstra(G,s,t)
    result_dijkstra_wanted = Dijkstra_wanted(G,t,s,r)
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = result_dijkstra[i] + result_dijkstra_wanted[i] - V[i]
    return min(result)
    """



def Dijkstra(G,s,t):
    lenght_G = len(G)+ 1
    P_Queue = PriorityQueue()
    dist = [ float('inf') for _ in range(lenght_G + 1)]
    dist[s] = 0
    P_Queue.put((dist[s],s))
    while not P_Queue.empty():
        node = P_Queue.get()
        current_node = node[1]
        if current_node == t:
            break
        for neighbour in (G[current_node]):
            vertice = neighbour[0]
            weight = neighbour[1]
            if dist[current_node] + weight < dist[vertice]:
                dist[vertice] = dist[current_node] + weight
                P_Queue.put((dist[vertice],vertice))
    return dist[t]
def Dijkstra_wanted(G,s,t,r):
    lenght_G = len(G) + 1
    P_Queue = PriorityQueue()
    dist = [float('inf') for _ in range(lenght_G + 1)]
    dist[s] = 0
    P_Queue.put((dist[s], s))
    while not P_Queue.empty():
        node = P_Queue.get()
        current_node = node[1]
        if current_node == t:
            break
        for neighbour in (G[current_node]):
            vertice = neighbour[0]
            weight = 2 * neighbour[1] + r
            if dist[current_node] + weight < dist[vertice]:
                dist[vertice] = dist[current_node] + weight
                P_Queue.put((dist[vertice], vertice))
    return dist[t]





def gold( G,V,s,t,r ):
    mini = float('inf')
    n = len(G)
    temp = 0
    for i in range(n):
        temp = Dijkstra(G,s,i) + Dijkstra_wanted(G,i,t,r) - V[i]
        mini = min(mini,temp)
    return mini"""

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )


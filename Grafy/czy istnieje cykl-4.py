"""
zadanie:
sprawdzić czy istnieje cykl mający 4 wierzchołki w grafie (skierowanym)
pomysł 1, ciężki do implementacji:
bierzemy każdy wierzchołek, sprawdzamy każdą ścieżkę długości 3 dla niego
w sensie bierzwemy każdy wierzchołek podpięty do pierwszego
dla każdego drugiego bierzemy wszystkie podpięte do niego
to samo dla trzeciego
dla każdego z tej ostatniej listy sprawdzamy czy istnieje powrót do pierwotnego
złożoność: O(n^3)
pomysł 2:
stosujemy reprezentacje macierzowa grafu
cykl 4 to kwadrat
bierzemy każdą parę
w szczególności zawsze znajdziemy przypadekw  którym 2 wierzchołki w parze leżą na przekątnej - nie ma krawędzi między nimi
w reprezentacji macierzowej przechodizmy po 2 wierszach tylko związanych z wierzchołkmai wybranymi w naszej parze
jeśli znajdziemy 2 inne punkty które mają krawędź z oboma punktami
"""
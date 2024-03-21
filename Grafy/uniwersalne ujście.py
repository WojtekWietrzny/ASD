"""
zadanie:
sprawdzamy czy w grafie (skierowanym) istnieje uniwersalne ujście
uniwersalne ujście - wierzchołek w grafu do którego istnieją krawędzie z każdego innego wierzchołka, ale z niego nie
wychodzi żadna krawędź
pomysł 1:
w reprezentacji macierzowej będzie w czasie n^2
sprawdzamy dla każdego wierzchołka czy ma krawędź do niego z każdego ( w kolumnie wchodzących same jedynki)
i czy z niego nic nie wychodzi (same 0 w drugiej kolumnie)

pomysł 2:
w reprezentacji macierzowej liniowo
idziemy od lewego górnego
jeśli zauważymy 0 to idziemy w prawo
jeśli napotkamy na 1 to idziemy w dół - jeśli dojdziemy na dół tą opcją to jest nasz podejrzany
sprawdzamy czy on działa w sposób opisany w pomyśle 1
"""
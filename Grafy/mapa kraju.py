"""
zadanie:
mamy mape kraju
miasta to wierzchołki między miastami są trasy ważone - odległość
na zmiane miedzy miastami jezdza alicja i bob
Alicja wybiera trase i to kto zaczyna jazde
chce to zrobic tak, zeby Alicja efektywnie przejechala najmniejsza liczbe kilometrów
algorytm ma zaproponować Alicji taką trasę

algorytm:
rozdawajamy każdy wierzchołek
np. jeśli mamy Xk i Xl i krawędź wagi w między nimi
to robimy sobie Xka, Xkb, Xla, Xlb i krawędź o wadze w będzie z Xka do Xlb i o wadze 0 z Xkb do Xla
z pewnego wierzchołka s do t znajdujemy najkrótszą dla Alicji w ten sposób, że szukamy - co dalej???

implementacja do domu
"""

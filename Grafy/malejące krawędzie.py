"""
zadanie:
każda krawędź ma przypisaną wagę ze zbioru {1,2,3....,|E| - liczba krawędzi}
pomysł:
modyfikujemy przeszukiwanie (wszerz):
jeśli wchodzimy do wierzchołka to pamiętamy z jakiego konkretnie do niego wchodziliśmy
albo po jakiej krawędzi do niego weszliśmy
chcemy żeby w kolejce krawędzie było w malejącej kolejności
to założenie o zakresie wag jest do tego żeby można było posortować liniowo

"""
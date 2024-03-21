"""
zadanie: mamy (p v ~q) ^ (~r v s) ^ (~s v q)
to jest postać konkiunkcyjna normalna
cnf - conjunctive normal form
2cnf - cnf ale są tylko 2 zmienne na klauzule
pytamy czy istnieje takie wartościowanie zmiennych, żeby to zdanie z góy miało wartość 1
rozwiązanie:
zamieniamy alternatywy na koniunkcje, kazda z nich zapisujemy w 2 strony
następnie implikacje zapisujemy jako krawędzie rgafu skierowanego
szukamy silnie spójnych składowych
następnie wiemy że w każdej takiej silnie spójnej składowej wszystkie zmienne muszą mieć wartość 0 albo wszystkie 1
możemy sobie ten graf uprościć i każdą z silnie spójnych przedstawić jako pewną wartość, 0 albo 1 - ale tą wartość
chcemy móc sobie wpisać dowolną, bo na tym polega zadanie
potem.... - dopisz
implementacja do domu
"""
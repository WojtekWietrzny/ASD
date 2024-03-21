"""
Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {1,...,n} na prostej.
Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
potrzebnych do pokrycia wszystkich punktów z X.
(Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch przedziałów,
np. [0.2, 1.2] oraz [1.4, 2.4]).
"""

def przedzialy(T):
    n = len(T)
    if not T:
        return 0
    if n == 1:
        return 1

    T.sort()
    last = T[0]
    counter = 1
    for i in range(1,n):
        if T[i] <= last + 1:
            continue
        last = T[i]
        counter += 1
    return counter

X = [-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]


print(przedzialy(X))
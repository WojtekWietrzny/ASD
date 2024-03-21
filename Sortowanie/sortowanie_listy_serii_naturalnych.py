"""
idea: dzielimy liste na kolejne serie naturalne
zadanie domowe
zaimplementować tą idee w sposób : odcinam 2 pierwsze serie, scalam, dodaje kolejna serie, znowu scalam, etc. (o(n^2))
i drugi sposób: dziele na pary, scalam 2 pierwsze, potem 3 i 4, potem kolejne 2 etc. tak scalam do końca (o(n*logn))
porównać te 2 sposoby na listach z 20 tysiącami elementów
"""
import random


def create_list(n):
    tab = []
    tab.append(random.randint(1,9))
    for i in range(1,n):
        tab.append(random.randint(0,9))
    return tab


tab = create_list(20000)
print(tab)
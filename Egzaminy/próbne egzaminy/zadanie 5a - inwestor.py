"""
idea na akceptowalną:
lecimy po każdym polu, traktujemy je jako początek pewnego przedziału
w tym przedziale szukamy minimum i mnożymy je razy liczbę wziętych pól
złożoność:
O(n^2) - przechodzi 5 testów
"""

def inwestor(T):
    n = len(T)
    inf = float('inf')
    result = 0
    for i in range(n):
        mini = inf
        quantity = 1
        for j in range(i,n):
            mini = min(mini,T[j])
            result = max(result, mini * quantity)
            quantity += 1
    return result

T = [2, 1, 5, 6, 2, 3]
print(inwestor(T))
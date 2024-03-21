"""
Zadanie 3: Rekurencyjne schody Amazona
Dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. Początkowo stoimy na pozycji 0,
wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję.
Przykład A = {1,3,2,1,0}
Z pozycji O mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4.
Należy policzyć na ile sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
idea:
przechodzimy bottom up po tablicy i dodajemy do pola na które możemy dojść,
liczbe możliwości dojścia na którym obecnie jesteśmy
"""

def amazon(A):
    n = len(A)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(n-1):
        for j in range(i+ 1, min(i + A[i] + 1,n)):
            dp[j] += dp[i]
    return dp[n-1]


import random

# A = [1, 3, 2, 1, 0]  # 4
# A = [2, 1, 3, 2, 1, 0]  # 8
A = [10, 6, 4, 4, 9, 10, 2, 3, 3, 6, 7, 7]


print('Input:', A)
print('Top-down: ', amazon(A))
print('Bottom-up:', amazon(A))
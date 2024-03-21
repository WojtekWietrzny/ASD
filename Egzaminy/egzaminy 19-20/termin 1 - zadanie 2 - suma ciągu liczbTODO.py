"""
idea:
podobne do mnożenia macierzy(?) - tak
"""

from zad2testy import runtests


def opt_sum(tab):
    n = len(tab)
    F = [[-float('inf') for i in range(n)] for j in range(n)]
    S = [0] * n
    S[0] = tab[0]

    for i in range(1, n):
        S[i] = S[i - 1] + tab[i]

    def sum(i, j):
        return S[j] - S[i] + tab[i]

    for i in range(n - 1):
        F[i][i + 1] = abs(tab[i + 1] + tab[i])

    for j in range(2, n):
        for i in range(n - j):
            minim = float('inf')
            for k in range(i, i + j):
                minim = min(minim, max(F[i][k], F[k + 1][i + j]))
            F[i][i + j] = max(minim, abs(sum(i, i + j)))

    return F[0][n - 1]


test_tabs = [[-999, -1000, 1001, 1000],
             [3, 2, -3, 4, 5, -9],
             [3, 6, 9, -8, -6, -3],
             [-1, 4, -6, 3, -4]]
print(opt_sum(test_tabs[0]))
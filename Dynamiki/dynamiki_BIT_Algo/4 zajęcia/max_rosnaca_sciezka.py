"""
Zadanie 5
Dostajemy tablicę (M x N) wypełnioną wartościami.
Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy (możemy przechodzić na pola sąsiadujące krawędziami),
o rosnących wartościach (to znaczy, że z pola o wartości 3, mogę przejść na pola o wartości większej bądź równej 4).
Na początku wprowadzimy pewne ułatwienie: Mamy dany punkt początkowy
"""


def longest_path(A: 'matrix of values', #podejście top down
                 M: 'number of rows',
                 N: 'number of columns',
                 P0: 'beginning point'):
    F = [[1] * N for _ in range(M)]
    i0, j0 = P0

    def move(i, j):
        if F[i][j] == 1:
            if i > 0 and A[i - 1][j] > A[i][j]:
                F[i][j] = max(F[i][j], move(i - 1, j) + 1)
            if i < M - 1 and A[i + 1][j] > A[i][j]:
                F[i][j] = max(F[i][j], move(i + 1, j) + 1)
            if j > 0 and A[i][j - 1] > A[i][j]:
                F[i][j] = max(F[i][j], move(i, j - 1) + 1)
            if j < N - 1 and A[i][j + 1] > A[i][j]:
                F[i][j] = max(F[i][j], move(i, j + 1) + 1)
        return F[i][j]

    res = move(i0, j0)

    return res
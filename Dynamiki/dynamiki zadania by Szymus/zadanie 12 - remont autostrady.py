"""
idea:
dokładnie ta sama co maximin, tylko odwrócona
nie tworzymy podciągów tak żeby najmniejszy z nich był jak największy
tylko żeby największy z nich był jak największy
czyli generalnie dzielimy autostrade na podciągi, każdy podciąg remontuje jedna firma
chcemy żeby suma podciągu o maksymalnej sumie, była możliwe najmniejsza
złożoność czasowa:
O(n^2k)
złożoność pamięciowa:
O(n^2)
"""

def maximin(T,k):
    n = len(T)
    inf = float('inf')
    dp = [[inf]*(k) for i in range(n)]#k- number of cuts
    S = [0]*n
    S[0] = T[0]#sums
    for i in range(1,n):
        S[i] = S[i-1] + T[i]

    for i in range(n):
        dp[i][0] = S[i]

    for x in range(1,k):#number of cuts
        for i in range(x,n):#last index
            for c in range(x-1,i):#mid point
                dp[i][x] = min(max(dp[c][x-1],S[i]-S[c]),dp[i][x])

    return dp[n-1][k-1]

def autostrada(A: 'sequence of numbers to split', k: 'number of splits'):
    print(A)
    print(k)
    if k == 0: return 0

    n = len(A)
    inf = float('inf')
    F = [[inf] * (k + 1) for _ in range(n)]

    # Fill the column for k = 1
    F[0][1] = A[0]
    for i in range(1, n):
        F[i][1] = F[i - 1][1] + A[i]

    # Sotore sums of values from 0 index to 'i' index
    S = [0] * n
    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]

    # Find the maximum value of the minimum split for each k value based
    # upon results for the previous subsequences and k values
    for t in range(2, k + 1):
        # We will consider all numbers up to a number at 'i' index (inclusive)
        for i in range(t - 1, n):
            # Loop over an index of the last number which will be included
            # in the first t - 1 splits
            for j in range(t - 2, i):
                F[i][t] = min(F[i][t], max(F[j][t - 1], S[i] - S[j]))


    return F[n - 1][k]


"""
idea:
patrzymy na to zadanie jak na ciągi rekurencyjne z dyskretnej
jeśli mamy na początku 0 to liczba jest nieprawidłowa
jeśli pojawia się zero i nie jest poprzedzone jedynką lub dwójką to też jest nieprawidłowe
jeśli dodamy się coś róznego od 0 i jest poprzedzone 0 to mamy tyle samo ciągów co przed jej dodaniem
jeśli nasze 2 ostatnie cyfry dają liczbę mniejszą niż 27 i większą lub równą 10, to znaczy że możemy dodać albo literę dwucyfrową
albo jednocyfrową

złożoność czasowa:
O(n)
złożoność pamięciowa:
O(n)
"""




"""
idea:
górny rząd i lewa kolumna mają jedną możliwość dojścia, albo tylko w prawo albo tylko w dół - wypełniamy
je odpowiednimi sumami wartości z tablicy
następnie albo idziemy na dane pole z lewej albo z góry, więc bierzemy minimum z wartości tych pól i dodajemy wartość obecnego
przechodzimy tak do ostatniego, zwracamy dp[n-1][n-1]
złożoność czasowa:
O(n^2)
złożoność pamięciowa:
O(n^2)
"""


def chess(A):
    n = len(A)
    dp = [[float('inf') for _ in range(n)]for _ in range(n)]
    dp[0][0] = A[0][0]
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + A[0][i]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + A[i][0]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + A[i][j]
    return dp[n-1][n-1]


















# nowa implementacja
def falisz(T):
    n = len(T)
    inf = float('inf')
    dp = [[inf for _ in range(n)] for _ in range(n)]
    dp[0][0] = T[0][0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + T[i][0]
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + T[0][i]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + T[i][j]
    return dp[n-1][n-1]
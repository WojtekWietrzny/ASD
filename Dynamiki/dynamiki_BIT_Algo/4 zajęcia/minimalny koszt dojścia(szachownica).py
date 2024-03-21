"""

Zadanie 4
Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia). Mamy znaleźć minimalny koszt potrzebny do dostania się z pozycji [0][0] do [M-1][N-1]
Zakładamy, że:
?
1. Możemy poruszać się tylko w prawo i w dół
2. Wszystkie koszty są dodatnie
idea:
ta sama co z kosztem poruszania się po szachownicy
"""

def chess(T):
    m = len(T)
    n = len(T[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = T[0][0]
    for i in range(1,m):
        dp[m][0] = dp[m-1][0] + T[m][0]
    for i in range(1,n):
        dp[0][n] = dp[0][n-1] + T[0][n]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + T[i][j]
    return dp[m-1][n-1]


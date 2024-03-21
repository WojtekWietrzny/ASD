"""
idea:
tablica dp[a][b] odpowiada na pytanie ile operacji potrzeba żeby z części słowa pierwszego
do indeksu a włącznie, zrobić część słowa drugiego do indeksu b włącznie
uzupełniamy zerowy wiersz i zerową kolumnę
indeks [0][0] wpisujemy ręcznie
potem przechodzimy po wierszach i odwołujemy się do pola na ukos w gore w lewo jeśli obecne na indeksach a i b litery są takie same
albo w pozostałych przypadkach do minimum z górnego, lewego i lewego górnego pola dodając 1, bo trzeba zamienić któreś
ze znaków pod indeksami a lub b
złożoność czasowa:
O(n^2)
złożoność pamięciowa:
O(n^2)
"""

def napraw(s,t):
    n = len(s)
    m = len(t)
    inf = float('inf')
    dp = [[0 for _ in range(n)] for _ in range(m)]
    if s[0] == t[0]:
        dp[0][0] = 0
    else:
        dp[0][0] = 1
    for i in range(1,n):
        if s[i] == t[0]:
            dp[0][i] = i
        else:
            dp[0][i] = dp[0][i-1] + 1
    for i in range(1,m):
        if s[0] == t[i]:
            dp[i][0] = i
        else:
            dp[i][0] = dp[i-1][0] + 1
    for i in range(1,m):
        for j in range(1,n):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    return dp[m-1][n-1]
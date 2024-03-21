"""
rozumiemy to zadanie jako pola na ktorych tankujemy
tablica dp[i] odpowiada na pytanie - jaki jest koszt dojechania do danego pola
wypełniamy dp[i] tak że bierzemy minimum z k indeksów w lewo i wartość T[i]
na koniec bierzemy minimum z k ostatnich indeksów
"""


def pretty_ksum(T,k):
    n = len(T)
    inf = float('inf')
    dp = [inf for _ in range(n)]

    for i in range(k):
        dp[i] = T[i]
    for i in range(k,n):
        mini = inf
        for j in range(i-k,i):
            mini = min(mini, dp[j])
        dp[i] = mini + T[i]

    mini = inf
    for i in range(n-1,n-k-1,-1):
        mini = min(mini, dp[i])
    return mini


#kod Filipa - 0,05
def ksuma(T, k):
    n = len(T)

    for i in range(k, n):
        T2 = T[i - k:i]
        mini = min(T2)
        T[i] += mini
    T2 = T[n - k:n]
    mini = min(T2)
    return mini

#kod Maćka - 0,38s
def ksuma( T, k ):
    n=len(T)
    inf = float('inf')
    dp=[inf]*n

    for i in range(k):
        dp[i] = T[i]

    for i in range(k,n):
        mini = inf
        for j in range(i-k,i):
            mini = min(mini,dp[j])

        dp[i] = T[i] + mini

    mini = inf
    for i in range(n-1,n-k-1,-1):
        mini = min(mini,dp[i])

    return mini



"""
rozumiemy to zadanie jako pola na ktorych tankujemy
tablica dp[i] odpowiada na pytanie - jaki jest koszt dojechania do danego pola
wypełniamy dp[i] tak że bierzemy minimum z k indeksów w lewo i wartość T[i]
na koniec bierzemy minimum z k ostatnich indeksów
"""

#nowa implementacja
def ksuma( T,k):
    n = len(T)
    inf = float('inf')
    dp = [inf for _ in range(n)]

    for i in range(k):
        dp[i] = T[i]
    for i in range(k, n):
        mini = inf
        for j in range(i-k,i):
            mini = min(mini,dp[j])
        dp[i] = T[i] + mini
    mini = inf
    for i in range(n-1,n-k-1,-1):
        mini = min(mini,dp[i])
    return mini













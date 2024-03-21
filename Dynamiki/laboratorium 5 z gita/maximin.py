"""
idea:
dzielimy na k ciągów i wynikiem jest najmniejsza z sum ciągów
żeby wynik był możliwie jak największy
"""


def maximin(T,k):
    n = len(T)
    dp = [[0]*(k) for i in range(n)]#k- number of cuts
    S = [0]*n
    S[0] = T[0]#sums
    for i in range(1,n):
        S[i] = S[i-1] + T[i]

    for i in range(n):
        dp[i][0] = S[i]

    for x in range(1,k):#number of cuts
        for i in range(x,n):#last index
            for c in range(x-1,i):#mid point
                dp[i][x] = max(min(dp[c][x-1],S[i]-S[c]),dp[i][x])

    return dp[n-1][k-1]

print(maximin([5, 2, 7, 1, 6, 3, 8, 4, 2, 7],3))
print(maximin([5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7],3))

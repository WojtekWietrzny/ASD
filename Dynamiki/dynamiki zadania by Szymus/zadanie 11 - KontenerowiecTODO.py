"""
idea:
robimy ta
"""

def kontenerowiec(T):
    mini = float('inf')
    n = len(T)
    S[0] = T[0]
    for i in range(1,n):
        S[i] = S[i-1] + T[i]
    sum = S[n-1]
    for i in range(n):
        for j in range(i+1,n):
            temp = S[j] - S[i]
            if i + j < n-1:
                mini = min(mini,abs(sum - temp - temp))
    return mini

# podejście 2
def kontenerowiec(T):
    inf = float('inf')
    n = len(T)
    dp = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        dp[i][i] = T[i]

    for i in range(1,n):
        for j in range(i,n):
            dp[i][j]= dp[i][j-1]
    sum = dp[0][n-1]
    mini = inf
    for i in range(n):
        for j in range(i,n):
            if i + j < n-1:
                temp = sum - dp[i][j]
                mini = min(mini,abs(temp - dp[i][j]))
    return mini

#podejście 3


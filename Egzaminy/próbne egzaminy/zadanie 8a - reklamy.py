"""
idea:
dynamik dp[i][0] lub dp[i][1]


"""


"""
idea na n^2:
biore maxa z 
"""

# rozwiązanie n^2
def reklamy(T,S,o):
    n = len(T)
    sum = 0
    max_sum =max(S)
    for i in range(n):
        sum = S[i]
        for j in range(i, n):
            if T[j][1] < T[i][0] or T[j][0] > T[i][1]:
                sum += S[j]
                if sum > max_sum:
                    max_sum = sum
                sum -= S[j]
    return max_sum


# rozwiązanie nlogn
def reklamy(T,S,o):
    n = len(T)
    P = [0 for _ in range(n)]
    for i in range(n):
        P[i] = (T[i][0], T[i][1], S[i])
    P.sort(key = lambda x: x[0])
    dp = [0 for _ in range(n)]
    dp[n-1] = P[n-1][2]
    for i in range(n-2, -1, -1):
        dp[i] = max(dp[i+1], P[i][2])

# dopisać bisect right


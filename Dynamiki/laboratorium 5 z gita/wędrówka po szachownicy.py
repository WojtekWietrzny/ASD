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

A = [
    [3, 4, 5, 2, 1],
    [7, 2, 13, 7, 8],
    [3, 1, 4, 1, 5],
    [2, 8, 11, 1, 3],
    [3, 5, 1, 3, 2]
]
print(chess(A))
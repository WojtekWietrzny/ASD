def knapsack(w,p,B):
    n = len(W)
    dp = [[0 for _ in range(B+1)] for _ in range(n)]
    for b in range(w[0], B+1):
        dp[0][b] = p[0]
    for b in range(w[0], B+1):
        for i in range(n):
            dp[i][b] = dp[i-1][b]
            if b - w[i] >= 0:
                dp[i][b] = max(dp[i][b],dp[i-1][b-w[i] + p[i]])
    return dp[n-1][B]
def dark_forest(A):
    n = len(A)
    dp = [0 for _ in range(n)]
    dp[0] = A[0]
    dp[1] = max(A[0],A[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2]+ A[i])
    return dp[n-1]

T = [8, 1, 3, 4, 5, 1, 2]

print(dark_forest(T))

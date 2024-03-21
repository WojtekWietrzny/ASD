def fall_guys(A):
    n = len(A)
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return n - max(dp)

ranges = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]

print(fall_guys(ranges))
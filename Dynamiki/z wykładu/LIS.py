# LIS n^2

def LIS(A):
    n = len(A)
    dp = [1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    result = []
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    maximum = -float('inf')
    start = 0
    for i in range(n):
        if dp[i] > maximum:
            maximum = dp[i]
            start = i
    i = start
    while i >= 0:
        result.append(A[i])
        if parent[i] != -1:
            i = parent[i]
        else:
            break
    result.reverse()
    return max(dp),result


A = [2,1,4,3,1,5,2,7,8,3]
print(LIS(A))

#LiS nlogn
"""
mamy dwie tablice i szukamy najdłuższego wspólnego podciągu
"""

def longest_common_subsequence(A,B):
    n = len(A)
    m = len(B)
    maximum = 0
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    for i in range(n+1):
        for j in range(m+1):
            maximum = max(maximum, dp[i][j])
    return maximum


a = 'aabcaca'
b = 'abaa'

print(longest_common_subsequence(a, b))




























#drugie podejście

def longest_common_subsequence(A,B):
    n = len(A)
    m =len(B)
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if A[i-1] == B[j-1]: # i - 1 z j - 1, żeby zniwelować bufor
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    maximum = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            maximum = max(maximum, dp[i][j])
    return maximum

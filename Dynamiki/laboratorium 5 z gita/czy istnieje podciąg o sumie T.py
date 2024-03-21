"""
idea:
tablica dp[i][T] przechowuje informacje czy za pomocą pierwszych i liczb można uzyskać sumę T
na początek jeśli za pomocą i-1 można to za pomocą i również można
dodatkowo jeśli dp[i][T] jest True to dp[i + A[i]][T] też jest True
"""
def subsequence(A,T):
    n = len(A)
    dp = [[False for _ in range(T+1)]for _ in range(n)]
    dp[0][A[0]] = True
    for i in range(1,n):
        for j in range(T+1):
            if dp[i-1][j] == True:
                dp[i][j] = True
                if j + A[i] < T+1:
                    dp[i][j + A[i]] = True
    if dp[n-1-1][T] == True: # jeśli nie działałoby to iteracja po wszystkich i przy ostatniej sumie, ale chyba musi działać
        return True
    return False

A = [2, 5, 1, 3, 7,8]
m = 19

print(subsequence(A, m))





























"""
idea:
tablica dp[i][T] przechowuje informacje czy za pomocą pierwszych i liczb można uzyskać sumę T
na początek jeśli za pomocą i-1 można to za pomocą i również można
dodatkowo jeśli dp[i][T] jest True to dp[i + A[i]][T] też jest True
"""

#drugie podejście

def subsequence(A,T):
    n = len(A)
    dp = [[False for _ in range(T)] for _ in range(n)]
    dp[0][A[0]] = True
    for i in range(1,n):
       for j in range(T+1):
            if dp[i-1][j] == True:
                dp[i][j] = True
            if j + A[i] <= T:
                dp[i][j + A[i]] = True
    return dp[n-1][T]

#mądrzej to napisałem niż za pierwszym xd


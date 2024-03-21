#dp[i][j] mówi ile minimalnie skoków potrzebujemy żeby dostać się z ilością energii i na pole j

def Zbigniew(A):
    n = len(A)
    inf = float('inf')
    dp = [[inf for _ in range(n)] for _ in range(n)]
    for j in range(n):
        dp[j][0] = 0
    for i in range(A[0]):
        dp[i][A[0]-i] = 1
    for i in range(n):
        for j in range(1,n):
            if dp[i][j] < inf:
                energy = min(n-j-1, i + A[j])
                for k in range(energy+1):
                    new_j = j + energy - k
                    dp[k][new_j] = min(dp[k][new_j], dp[i][j] + 1)
    return dp[0][n-1]

A = [2, 3, 1, 1, 2, 0]
print(Zbigniew(A))

# generalnie w ogóle żabe można w O(n^2) zachłannie xd
#dynamik jest O(n^3)
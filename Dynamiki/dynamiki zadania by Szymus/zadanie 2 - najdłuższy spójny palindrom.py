"""
idea:
chuj wie jak to dynamicznie zrobić - XD
do dokończenia
"""



def palindrom( S ):
    n = len(S)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n):
        for j in range(n):
            if i == j + 1 or j == i + 1:
                if S[i] == S[j]:
                    dp[i][j] = True
                    dp[j][i] = True
                else:
                    dp[i][j] = False
                    dp[j][i] = False
    print("pierwsza pętla")
    print(dp)
    for i in range(n):
        for j in range(n):
            if S[i] != S[j] and not dp[i][j]:
                dp[i][j] = False
            elif not dp[i][j] and S[i] == S[j] and i + 1 <=n-1 and j-1 >= 0:
                dp[i][j] = dp[i + 1][j - 1]
    print("druga pętla")
    print(dp)
    max_lenght = 0
    palindrom = [0, 0]
    for i in range(n):
        for j in range(i,n):
            if dp[i][j] == True:
                if j - i + 1 > max_lenght:
                    max_lenght = j - 1 + 1
                    palindrom = [i, j]
    x = palindrom[0]
    y = palindrom[1]
    return S[x:y+1]

S = 'abbaabbc'

print(palindrom(S))

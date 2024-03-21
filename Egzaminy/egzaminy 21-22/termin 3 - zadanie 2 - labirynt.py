"""
idea:
uzupełniamy lewą kolumnę, na każde pole można się dostać tylko z dołu i lewej, albo góry i lewej, więc tworzymy tablicę
up i down, potem bierzemy maxa z nich
"""

def maze(L):
    n = len(L)
    dp = [[[-1, -1] for _ in range(n)] for _ in range(n)]  # [from up, from down]
    dp[0][0] = [0,0]
    for i in range(1, n):
        if L[i][0] == "#":
            break

        dp[i][0][0] = i

    for i in range(1, n):
        if L[0][i] == "#":
            break

        dp[0][i][0] = i

    for j in range(1, n):
        for i in range(n):
            if L[i][j] == "#":
                continue
            if i == 0:
                dp[i][j][0] = max(dp[i][j - 1][0],dp[i][j-1][1]) + 1
            else:
                dp[i][j][0] = max(dp[i][j - 1][0],dp[i][j-1][1],dp[i-1][j][0]) + 1
            if dp[i][j][0] == 0:
                dp[i][j][0] = -1
        for k in range(n - 1, -1, -1):
            if L[k][j] == "#":
                continue
            if k == n-1:
                dp[k][j][1] = max(dp[k][j - 1][0], dp[k][j - 1][1]) + 1
            else:
                dp[k][j][1] = max(dp[k][j - 1][0], dp[k][j - 1][1], dp[k + 1][j][1]) + 1
            if dp[k][j][1] == 0:
                dp[k][j][1] = -1
    return max(dp[n - 1][n - 1][0],dp[n-1][n-1][1])









#nowe podejście
"""
idea:
uzupełniamy lewą kolumnę, na każde pole można się dostać tylko z dołu i lewej, albo góry i lewej, więc tworzymy tablicę
up i down, potem bierzemy maxa z nich
"""

def maze(L):
    n = len(L)
    dp = [[[-1,-1] for _ in range(n) ] for _ in range(n)] # from up, from down
    dp[0][0] = [0,0]

    for i in range(1, n): # uzupełniamy kolumnę
        if L[i][0] == "#":
            break

        dp[i][0][0] = i

    for i in range(1, n): # uzupełniamy rząd
        if L[0][i] == "#":
            break

        dp[0][i][0] = i

    for j in range(1,n):
        for i in range(n): # uzupełnianie from up
            if L[i][j] == "#": # szukamy niedostępnego pola
                continue
            if i == 0:
                dp[i][j][0] = max(dp[i][j-1][0],dp[i][j-1][1]) + 1 # tylko opcje z lewej
            else:
                dp[i][j][0] = max(dp[i][j-1][0],dp[i][j-1][1],dp[i-1][j][0]) + 1 # z lewej i z góry
            if dp[i][j][0] == 0: # jeśli jest 0 to było -1 i +1, czyli na pole nie da się dostać
                dp[i][j][0] = -1
        for k in range(n-1,-1,-1): # uzupełnianie from down
            if L[k][j] == "#": # szukamy niedostępnego pola
                continue
            if k == n-1:
                dp[k][j][1] = max(dp[k][j-1][1],dp[k][j-1][0]) + 1 # tylko z lewej
            else:
                dp[k][j][1] = max(dp[k][j-1][1],dp[k][j-1][0],dp[k+1][j][1]) + 1 # z lewej i z dołu
            if dp[k][j][1] == 0: # jeśli jest 0 to było -1 i +1, czyli na pole nie da się dostać
                dp[k][j][1] = -1
    return max(dp[n-1][n-1][0], dp[n-1][n-1][1])



















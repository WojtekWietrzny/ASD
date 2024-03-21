"""
idea:
dp[i] to krotka postaci (ilość zer, ilość jedynek) zsumowanych włącznie do indeksu i
zliczamy zera i jedynki
dla każdego możliwego ciągu obliczamy ilość zer i jedynek posługując się tablicą dynamiczną i różnicami
znajdujemy maksymalną różnicę
złożoność czasowa:
O(n^2)
złożoność pamięciowa:
O(n) - chyba? czy tablice krotek liczymy jako n^2
"""


"""def roznica( S ):
    n = len(S)
    dp = [0 for _ in range(n)]
    max_difference = - 1
    max_length = 0
    if S[0] == 0:
        dp[0] = (1,0) #krotka postaci (liczba zer, liczba jedynek)
    else:
        dp[0] = (0,1)
    for i in range(1,n): # uzupełniam każdy element tablicy ilością zer i jedynek od 0 do i w krotce
        if S[i] == '0':
            dp[i] = (dp[i-1][0]+1,dp[i-1][1])
        else:
            dp[i] = (dp[i - 1][0], dp[i - 1][1]+1)
    print(dp)

    if dp[n-1][0] == 0:
        return -1


    for i in range(n):
        for j in range(i+1,n):
            zeros = dp[j][0] - dp[i][0] + 1
            ones = dp[j][1] - dp[i][1] + 1
            max_difference = max(zeros - ones, max_difference)

    return max_difference"""\














"""
idea:
dp[i] to krotka postaci (ilość zer, ilość jedynek) zsumowanych włącznie do indeksu i
zliczamy zera i jedynki
dla każdego możliwego ciągu obliczamy ilość zer i jedynek posługując się tablicą dynamiczną i różnicami
znajdujemy maksymalną różnicę
złożoność czasowa:
O(n^2)
złożoność pamięciowa:
O(n) - chyba? czy tablice krotek liczymy jako n^2
"""

def roznica(S):
    n  =len(S)
    dp = [0 for _ in range(s)]
    zeros = 0
    ones = 0
    for i in range(n):
        if S[i] == 0:
            zeros += 1
        else:
            ones += 1
        dp[i] = (zeros,ones)
    for i in range(n):
        for j in range(i,n):
            zeros_num = dp[j][0] - dp[i][0]
            ones_num = dp[j][1] - dp[i][1]
            max_dif = max(max_dif,zeros - ones)
    if dp[n-1][0] == 0:
        return -1
    return max_dif

















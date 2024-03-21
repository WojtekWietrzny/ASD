
"""
WOJCIECH WIETRZNY 415792
opis algorytmu:
rozważam w problemie funkcje dp[i][j] odpowiadającą na pytanie, jaki jest najmniejszy koszt
złożoność czasowa:
O(n*E)
złożoność pamięciowa:
O(n*E)
"""




def planets(D,C,T,E):
    inf = float("inf")
    n = len(D)
    dp = [[inf for _ in range(E+1)] for _ in range(n)]
    dp[0][0] = 0
    dp[T[0][0]][0] = T[0][1]

    for i in range(E+1):
        dp[0][i] = i * C[0]
    for i in range(1,n):
        dist = D[i] - D[i - 1]
        for j in range(E+1):
            if j + dist <= E: # przelecenie bez tankowania z poprzedniej
                dp[i][j] = min(dp[i][j], dp[i-1][j+dist])
            if j == 0: # teleport
                if T[i][0] > i:
                    dp[T[i][0]][0] = min(dp[T[i][0]][0], dp[i][0] + T[i][1])
            dp[i][j] = min(dp[i][j], dp[i][j-1] + C[i]) # tankowanie, to już daje wzorcówkę
            # na akceptowalną leci się tu pętlę
    return dp[n-1][0]

D = [0, 5, 10, 20]
C = [2, 1, 3, 8]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E = 10
print(planets(D,C,T,E))

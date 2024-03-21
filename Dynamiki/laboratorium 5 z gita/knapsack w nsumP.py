"zadanie plecakowe - jaka jest minimalna cena pozwalająca osiągnąć dany profit?"

def filter(W,P,max_W):
    n = len(W)
    new_W = []
    new_P = []
    for i in range(n):
        if P[i] > 0 and W[i] <= max_W:
            new_P.append(P[i])
            new_W.append(W[i])
    return new_W, new_P

def knapsack(W,P,max_W):
    W,P = filter(W,P,max_W)
    max_P = 0
    n = len(W)
    for i in range(n):
        max_P += P[i]

    dp = [[max_W+1 for _ in range(max_P+1)] for _ in range(n)] # wiersze to indeksy przedmiotów, kolumny to osiągane profity
    for p in range(P[0]+1): # wypełniamy dla pierwszego przedmiotu
        dp[0][p] = W[0]
    for i in range(1,n):
        for p in range(max_P+1):
            dp[i][p] = dp[i-1][p]
            if P[i] >= p and W[i] <= dp[i-1][p]:
                dp[i][p] = W[i]
            elif P[i] < p and dp[i-1][p-P[i]]+W[i] <= max_W:
                dp[i][p] = min(dp[i-1][p],dp[i-1][p-P[i]] + W[i])
    for p in range(max_P,-1,-1):
        if dp[n-1][p] <= max_W:
            return p
    return 0

P = [5, 3, 8, 4, 1]
W = [60, 50, 115, 70, 5]
MaxW = 115

print(knapsack(W, P, MaxW))
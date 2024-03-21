"""
idea:
zbieramy wartości potrzebne do podlania każdego drzewa w tablicy jednowymiarowej, gdzie dp[i]
określa ilość wody potrzebną do podlania drzewa w lokalizacji i
problem plecakowy?
złożoność czasowa:

złożoność pamięciowa:

"""
#TODO
def print_new(T):
    n = len(T)
    for i in range(n):
        print(T[i])


"""def gardener(T):
    n = len(T)
    m = len(T[0])
    T2_value = [0 for _ in range(m)]
    T2_bool = [[False for _ in range(m)] for _ in range(n)]
    def trees(T,T2_value,k,i,j):
        nonlocal T2_bool
        nonlocal n
        nonlocal m
        T2_value[k] += T[i][j]
        print(T2_value)
        T2_bool[i][j] = True
        if i-1 >= 0 and T2_bool[i-1][j] == False and T[i-1][j]:
            return trees(T,T2_value,k,i-1,j)
        if i + 1 < n and T2_bool[i + 1][j] == False and T[i+1][j]:
            return trees(T,T2_value,k,i+1,j)
        if j - 1  >= 0 and T2_bool[i][j - 1] == False and T[i][j-1]:
            return trees(T,T2_value,k,i,j-1)
        if j + 1 < m and T2_bool[i][j + 1] == False and T[i][j+1]:
            return trees(T,T2_value,k,i,j+1)
    for i in range(m):
        T2_value[i] = trees(T,T2_value,i,0,i)
    print_new(T2_bool)
    print(T2_value)
    return T2_value"""
def knapsack(w,p,B):
    n = len(w)
    dp = [[0 for _ in range(B+1)] for _ in range(n)]
    for b in range(w[0], B+1):
        dp[0][b] = p[0]
    for b in range(w[0], B+1):
        for i in range(n):
            dp[i][b] = dp[i-1][b]
            if b - w[i] >= 0:
                dp[i][b] = max(dp[i][b],dp[i-1][b-w[i] + p[i]])
    return dp[n-1][B]

def water(T,j):
    n = len(T)
    m = len(T[0])
    ammount = 0
    def fill(i,j):
        nonlocal n
        nonlocal m
        nonlocal ammount
        ammount += T[i][j]
        T[i][j] = 0
        if i-1 >= 0  and T[i-1][j] > 0:
            fill(i-1,j)
        if i + 1 < n  and T[i+1][j] > 0:
            fill(i+1,j)
        if j - 1  >= 0  and T[i][j-1] >0:
            fill(i,j-1)
        if j + 1 < m and T[i][j+1] > 0:
            fill(i,j+1)
    fill(0,j)
    return ammount

def gardener(T,D,Z,l):
    n = len(T)
    m = len(T[0])
    T_new = []
    for element in D:
        T_new.append(water(T,element))
        Z_new = []
    for i in range(n):
        if Z[i] > 0:
            Z_new.append(Z[i])

    dp = [[0 for _ in range(l+1)] for _ in range(len(T_new))]
    n = len(T_new)
    for b in range(T_new[0], l+1):
        dp[0][b] = Z[0]
    for b in range(T_new[0], l+1):
        for i in range(n):
            dp[i][b] = dp[i-1][b]
            if b - T_new[i] >= 0:
                dp[i][b] = max(dp[i][b],dp[i-1][b-T_new[i] + Z[i]])
    return dp[n-1][l]


T = [
    [0,0,0,0,1,0,0,0,0,5,0,0,1,0,0,0,4,0,0,0],
    [0,0,0,0,2,0,0,0,0,6,0,0,2,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,3,1,0,0,2,2,2,0,2,4,2,0],
    [0,0,0,1,2,0,0,1,4,6,0,2,1,3,0,0,3,1,0,0]
]
D = [4,9,12,16]
Z = [13,11,15,4]
l = 32

print(gardener(T,D,Z,l))

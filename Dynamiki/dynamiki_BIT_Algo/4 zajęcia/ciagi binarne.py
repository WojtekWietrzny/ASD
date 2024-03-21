"""
Zadanie 6
Dostajemy liczbę naturalną n. Naszym
zadaniem jest policzenie wszystkich binarnych (0/1)
string'ów o długości n bez jedynek obok siebie
"""

def binary(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

for n in range(11):
    print(binary(n), end=' ')
"""
idea:
dla każdej długości pręta cofam się o maksymalną liczbę pól jaką mogę i sprawdzam po kolei
dołożenie jakiej długości uciętego fragmentu do poprzedniego zysku z mniejszego pręta da najlepszy zysk


"""

def rod_cutting(n,P):
    dp = [0 for _ in range(n+1)]
    dp[0] = P[0]

    for i in range(n+1):
        for j in range(i):
            dp[i] = max(dp[i], P[i-j] + dp[j])
    return dp[n]

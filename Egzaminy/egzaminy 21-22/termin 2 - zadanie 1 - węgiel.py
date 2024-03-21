"""
idea:
przechodzimy na pałe dla każdego transportu węgla od lewej po magazynach i sprawdzamy gdzie się zmieści
jeśli się zmieści to tam go wrzucamy i przechodzimy do kolejnego transportu węgla
złożoność czasowa:
O(n^2)
złożoność pamięciowa:
O(n)
"""

def coal (A,T):
    n = len(A)
    dp = [T for _ in range(n)] # ile miejsca zostało
    curr = 0 # do którego magazynu wjechał obecny transport
    for i in range(n):
        for j in range(n):
            if A[i] <= dp[j]:
                curr = j
                dp[j] -= A[i]
                break
    return curr



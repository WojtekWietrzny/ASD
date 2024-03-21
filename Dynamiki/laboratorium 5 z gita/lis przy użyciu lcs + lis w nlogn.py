"""
lis przy użyciu LCS, pierwsza tablica to ciąg, w którym szukamy podciągu rosnącego
druga tablica to będzie posortowana pierwsza
"""

def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    maximum = 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(n + 1):
        for j in range(m + 1):
            maximum = max(maximum, dp[i][j])
    return maximum

def create_second_sequence(A):
    A_sorted = [*A]
    # Sort an array
    A_sorted.sort()
    # Filter out repeated values
    A_cp = [A_sorted[0]]
    for i in range(1, len(A)):
        if A_sorted[i] != A_sorted[i - 1]:
            A_cp.append(A_sorted[i])
    return A_cp


def lis_with_lcs(A):
    B = create_second_sequence(A)
    print(B)
    return longest_common_subsequence(A,B)

a = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3]
print(lis_with_lcs(a))


"""
longest increasing subsequence w O(n*logn)
"""


# 6.

def binary_search(A, val):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if val > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


def lis(A):
    n = len(A)
    last = []

    for i in range(n):
        idx = binary_search(last, A[i])

        if idx == len(last):
            last.append(A[i])
        else:
            last[idx] = A[i]

    return len(last)
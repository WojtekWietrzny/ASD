#1 opcja, dla liczb całkowitych
def binary_search_first(arr,val):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r)//2
        if val < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if r >= 0 and arr[r] == val:
        return r
    else:
        return -1

def filter_intervals(arr, target):
    A_filtered = []
    for element in A:
        if element[0] >= target [0] and element[1] <= target[1]:
            A_filtered.append(element)
    return A_filtered

def intervals(A, target):
    a,b = target
    c = b-a + 1
    dp = [[None for _ in range(c)] for _ in range(c)]
    A = filter_intervals(A,target)
    A.sort()
    def can_merge(i,j):
        if dp[i-a][j-a] is not None:
            return dp[i-a][j-a]
        if binary_search_first(A,[i,j]) >= 0:
            dp[i-a][j-a] = True
            return True
        dp[i-a][j-a] = False
        for k in range(i+1,j):
            dp[i-a][j-a] = can_merge(i,k) and can_merge(k,j)
            if dp[i-a][j-a]:
                break
        return dp[i-a][j-a]
    return can_merge(a,b)


"""A = [[4, 5], [2, 4], [1, 3], [3, 6], [5, 7], [1, 5], [-5, 2]]

print(intervals(A, [1, 7]))
print(intervals(A, [2, 5]))
print(intervals(A, [-5, 5]))
print(intervals(A, [0, 2]))"""

#2 TODO

#3 TODO

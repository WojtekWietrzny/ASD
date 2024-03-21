def partition(A, p,r):  # można jako pivota (x) wrzucić medianę dowolnych 3 elementów tablicy i już będzie gwarantowane nlogn
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def select(A, p, r, k):
    if p == r:
        return A[p]
    if k >= p and k <= r:
        q = partition(A, p, r)
        if k == q:
            return A[q]
        elif q > k:
            return select(A,p,q-1,k)
        else:
            return select(A,q+1,r,k)


def quick_select(T, p, r, k):  # k largest
    if p == r:
        return T[p]

    if k >= p and k <= r:
        q = partition(T, p, r)

        if k == q:
            return T[q]

        elif q > k:
            return quick_select(T, p, q - 1, k)

        else:
            return quick_select(T, q + 1, r, k)
def select_iter(A,p,q,k):
    n = len(A)
    while p <= q:
        x = partition(A,p,q)
        if x == k:
            return A[k]
        elif k > x:
            p = x + 1
        else:
            q = x-1
tab = [1,2,5,3,6,7,3,9]
n = len(tab)
print(select(tab,0,n-1,3))
"""
select(A,0) = min(A)
select(A,len(A) - 1) = max(A)
select(A, len(A)/2) = mediana A
"""




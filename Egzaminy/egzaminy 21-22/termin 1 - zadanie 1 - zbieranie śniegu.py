def snow( S ):
    def quick_sort(T,p,r):
        if p < r:
            q = partition(T,p,r)
            if T[q] < q:
                quick_sort(T,p,q-1)
            else:
                quick_sort(T,p,q-1)
                quick_sort(T,q+1,r)
    def partition(T, p, r):
        x = T[r]
        i = p-1
        for j in range(p,r):
            if T[j] >= x:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i+1], T[r] = T[r], T[i+1]
        return i+1

    n = len(S)
    quick_sort(S,0,n-1)
    sum = 0
    i = 0
    while S[i] > i:
        sum += S[i] - i
        i += 1
    return sum
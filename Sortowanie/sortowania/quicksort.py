def quicksort(A,p,r,key):
    if p < r:
        q = partition(A,p,r,key)
        quicksort(A,p,q-1,key)
        quicksort(A,q+1,r,key)

def partition(A,p,r,key): # można zjako pivota (x) wrzucić medianę dowolnych 3 elementów tablicy i już będzie gwarantowane nlogn
    x = A[r][key]
    i = p - 1
    for j in range(p,r):
        if A[j][key] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def altered_partition(T,p,r,key):
    x = T[r][key]
    i = p-1
    for j in range(p,r):
        if T[j][key] <= x:
            i+=1
            T[i],T[j] = T[j],T[i] 
    T[i+1],T[r] = T[r], T[i+1] 
    return i+1

def altered_quicksort(T,p,r,key):
    while p<r:
        q = altered_partition(T,p,r,key)
        if (q-1) - p > r-(q+1):
            altered_quicksort(T,p,q-1,key)
            p = q+1
        else:
            altered_quicksort(T,q+1,r,key)
            r = q-1
tab = [(21,4),(13,2),(12,3),(10,5),(8,1)]
n = len(tab)
quicksort(tab,0,n-1,0)
print(tab)
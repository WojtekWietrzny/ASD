def merge(T,p,q,r):
    L=T[p:q+1]
    R=T[q+1:r+1]

    L+=[float('inf')]
    R+=[float('inf')]

    i=0#iterator L
    j=0#iterator R

    for k in range(r-p+1):
        if L[i]<=R[j]:
            T[p+k]=L[i]
            i+=1

        else:
            T[p+k]=R[j]
            j+=1

def merge_sort(T,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(T,p,q)
        merge_sort(T,q+1,r)
        merge_altered(T,p,q,r,key)
def merge_altered(T,p,q,r,key):
    L=T[p:q+1]
    R=T[q+1:r+1]

    L+=[tuple('inf')]
    R+=[tuple('inf')]

    i=0#iterator L
    j=0#iterator R

    for k in range(r-p+1):
        if L[i][key]<=R[j][key]:
            T[p+k]=L[i]
            i+=1

        else:
            T[p+k]=R[j]
            j+=1

"""def merge_sort_altered(T,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(T,p,q)
        merge_sort(T,q+1,r)
        merge(T,p,q,r)"""

def merge_sort_altered(arr,key):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort_altered(left,key)
    merge_sort_altered(right,key)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
tab=[(3,9),(2,8),(7,7),(4,6),(5,5),(6,4),(9,3),(8,2),(1,1)]
n=len(tab)
merge_sort_altered(tab,1)
print(tab)
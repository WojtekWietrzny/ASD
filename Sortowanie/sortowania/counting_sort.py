def counting_sort_index(A,k,key):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i][key]] += 1
    for i in range(1,k):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i][key]]-1] = A[i]
        C[A[i][key]] -= 1
    for i in range(n):
        A[i] = B[i]

def counting_sort(A,k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1,k):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]
tab=[(3,9),(2,8),(7,7),(4,6),(5,5),(6,4),(9,3),(8,2),(1,1)]
data = [121, 432, 564, 23, 1, 45, 788]
n=len(tab)
counting_sort_index(tab,10,1)
counting_sort(data,800)
print(tab)
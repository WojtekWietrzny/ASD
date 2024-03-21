class Node:
    def __init__(self,val,next = 0):
        self.val = val
        self.next = next

def left(i):
    return 2*i +1
def right(i):
    return 2*i + 2
def parent(i):
    return (i-1)//2
def heapify(A,i,n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] < A[max_ind]:
        max_ind = l
    if r < n and A[r] < A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,max_ind,n)
def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A,i,n)
def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i],A[0]
        heapify(A,0,i)
def insert(T,el,n):
    T.append(el)
    heapify(T,0,n)
def extract_min(tab):
    return tab[0]

a = Node(11)
b = Node(7)
c = Node(9)
d = Node(10)
e = Node(17)

a.next = b
b.next = c
c.next = d
d.next = e

"""tab = [1,11,2,3,4,5,6,7,8,9]
heap_sort(tab)
print(tab)
tab = []"""
def k_list(k):
    g = Node(0,a)
    n = 0
    while g.next is not None:
        n += 1
        g = g.next
    g = Node(0)
    g.next = a
    p = g
    x = Node(a, a.next)
    tab = [0] * k
    for i in range(k):
        insert(tab,x,k)
        heapify(tab,0,k)
        x = x.next
    for i in range(n-k):
        p.next = Node(extract_min(tab))
        insert(tab,x,k)
        x = x.next
        heapify(tab,0,k)
    for i in range(k):
        p.next = Node(extract_min(tab))
        insert(tab,inf,k)
    return g.next
k_list(3)

for i in range(5):
    print(a.val)
    a = a.next

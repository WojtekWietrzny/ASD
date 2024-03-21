"""
zaimplementować Heap Sort
"""

def swap(a,b):
    temp = a
    a = b
    b = temp

def insert(T,el):
    n = len(T)
    T.append(el)
    heapify(T,p)


def parent(i):
    return (i-1)//2
def left(i):
    return 2*i +1
def right(i):
    return 2*i +2
def heapify(T,i):
    p = parent(i)
    if i != 0 and T[i] > T[p]:
        heapify(T,p)

heap = [13,9,8,7]
insert(heap, 15)
print(heap)
"""
nie potrzebujemy warunków końca, bo dojdzie do miejsca 
"""

"""l = left(i)
    r = right(i)
    maxi = i
    if l <= size and T[l] > T[maxi]:
        maxi = l
    if r < size and T[r] > T[maxi]:
        maxi = r
        if maxi != i:
            swap(T[i], T[maxi])
            heapify(T,maxi,size)
to jest heapify do usuwania            
"""
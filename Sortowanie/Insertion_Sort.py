def insertion_sort(T):
    l = range(T)
    for i in range(l):
        for j in range(i, 0, -1):
            if T[j-1] > T[j]:
                temp = T[j-1]
                T[j-1] = T[j]
                T[j] = temp
"""
przy stałej ilości (niezależnej od n elementów nieposortowanych, insertion sort będzie miał złożoność liniową
przy częściowo źle posortowanych tablicach insertion sort może być dobrze działający
"""
#z listy jednokierunkowej nieposortowanej usuwamy maksimum
class Node:
    def __init__(self,v,next):
        self.v = v
        self.next = next

def remove_max(head):
    m = head.next.val
    mptr = head
    p = mptr.next
    while p.next is not None:
        if p.next.v > m:
            mptr = p
            m = p.next.val
        p = p.next
    ret = mptr.next
    mptr.next = mptr.next.next
    return ret

#do listy wtawiamy w odpowiednie miejsce
class Node:
    def __init__(self, v, next=None):
        self.v = v
        self.next = next

def insert(head, n): # n - element do wstawienia, zwracamy wskaźnik na pierwszy element listy, za
    p = head
    while p.next is not None and p.next.v < n.val:
        p = p.next
    n.next = p.next
    p.next = n

# implementujemy insertion sorta za pomocą dwóch funkcji znajdujących się wyżej
# odpinamy z listy pierwotnej i dopinamy na listę posortowaną

def i_sort(head):
    sorted = Node(None,None)
    while head.next is not None:
        p = head.next
        p.next = None
        head.next = head.next.next
        sorted = insert(head,p)
    return sorted
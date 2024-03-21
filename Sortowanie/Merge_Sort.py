"""
implementujemy merge sorta
"""
class Node:
    def __init__(self,v,next):
        self.v = v
        self.next = next


def l_merge(L1, L2):
    if L1 == None:
        return L2
    if L2 == None:
        return L1
    head,tail = None,None
    while L1 != None and L2 != None:
        if L1.v < L2.v:
            tmp = L1
            L1 = L1.next
        else:
            tmp = L2
            L2 = L2.next
        if tail == None:
            tail = tmp
            head = tmp
        else:
            tail.next = tmp
            tail = tail.next
        tail.next = None
    if L1 != None:
        tail.next = L1
    else:
        tail.next = L2
    return head

def N_series(L):
    curr = L
    while curr.next != None and curr.v <= curr.next.v:
        curr = curr.next
    rest = curr.next
    curr.next = None
    return L, rest


def merge_sort(l):
    while True:
        l, tail = head, None
        counter = 0
        while l is not None:
            s1, l = N_series(l)
            if l is None and counter == 0:
                return s1
            counter += 1
            if l is None:
                tail.next = s1
                l = head
                break
            s2, l = N_series(l)
            merged = lmerge(s1, s2)
            if head is None:
                head = merged
                tail = merged
            else:
                tail.next = merged
            while tail.next is not None:
                tail = tail.next

# dokończyć implementacje w domu

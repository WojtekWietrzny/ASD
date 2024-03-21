




class Node:
    def __init__(self, v, next=None):
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
#funkcja usuwa pierwszą serie naturalna z listy i zwraca wskazanie na glowe usunietej listy i glowe nowej listy
#
class Node:
    def __init__(self,v,next=None):
        self.v = v
        self.next = next

def N_series(L):
    curr =L
    while curr.next != None and curr.v <= curr.next.v:
        curr = curr.next
    rest = curr.next
    curr.next = None
    return L,rest
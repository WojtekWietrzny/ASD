"""
zaimplementować Partition Hoevre'a
partition to było wykorzystywane w quick sorcie bez rekurencji
"""

def Partition(tab,left,right):
    l = left
    r = right
    pivot = right
    while l < r:
        while tab[l] < tab [pivot]:
            l += 1
        while tab[r] > tab[pivot] and l < r:
            r -= 1
        tab[l], tab[r] = tab[r], tab[l]
    tab[l], tab[pivot] = tab[pivot], tab[l]
    return l
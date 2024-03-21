"""
zaimplementować QS bez rekurencji
"""

def partition(tab,left,right):
    l = left
    r = right - 1
    pivot = right
    while l < r:
        while tab[l] < tab [pivot]:
            l += 1
        while tab[r] > tab[pivot] and l < r:
            r -= 1
        tab[l], tab[r] = tab[r], tab[l]
    if tab[l] > tab[pivot]:
        middle = l
    else:
        middle = l + 1

    tab[middle], tab[pivot] = tab[pivot], tab[middle]
    return l

def quick_sort(T):
    n = len(T)
    stack = [(0, n - 1)]
    while len(stack) != 0:
        a, b = stack.pop()
        print(a,b)
        if a < b:
            s = partition(T, a, b) # metoda zajmująca się podzieleniem tablicy na 2 części, jedną z elementami mniejszymi od dzielącego, drugą z większymi
            stack.append((a, s - 1))
            stack.append((s + 1, b))

    print(T)


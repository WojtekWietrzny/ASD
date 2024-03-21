"""
dana jest lista w której dane przyjmują wartości od 0 do k-1
szukamy najkrótszego podciagu spojnego przyjmujacego wszystkie wartosci
"""


"""
idea algorytmu:
dodajemy wartości do podanych indeksów w tablicy
i idzie od lewej, j od prawej
zmniejszamy j dopóki nie wyjdzie jakiś indeks równy 0
za każdym razem zmniejszając j sprawdzamy czy indeks z którego odejmujemy nie jest równy 0

"""
def podciag(tab,k):
    n = len(tab)
    C = [0 for _ in range(k)]
    for i in range(n):
        C[tab[i]] += 1
    i = 0
    j = n-1
    mini = 0
    while i < j and i < n and j < n:
        while C[tab[j]-1] != 1:
            C[tab[j]-1] -= 1
            j -= 1
        if j-i + 1 < mini:
            mini = j - i + 1
        while C[tab[i]-1] != 1:
            C[tab[i]-1] -= 1
            i += 1
        if j-i + 1 < mini:
            mini = j - i + 1
    return mini

tab = [1,2,3,4,5,5,3,4,2,5]
#print(podciag(tab,5))



# rozwiązanie Maćka

def find(T,k):
    n=len(T)
    elements=[0 for i in range(k)]

    for i in range(n):
        elements[T[i]]+=1

    if min(elements)==0:
        return -1

    j=n-1
    while elements[T[j]]>1:
        elements[T[j]]-=1
        j-=1

    mini = j+1

    for i in range(1,n-k+1):
        elements[T[i-1]]-=1
        if elements[T[i-1]]>0:
            mini=j-i+1

        else:
            while j<n-1 and elements[T[i-1]]==0:
                j+=1
                elements[T[j]]+=1

            if elements[T[i-1]]==0:
                return mini

            mini=min(mini,j+i-1)

    return mini


print(find([0,2,2,1,1,0,1,1,2],3))

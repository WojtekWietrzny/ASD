def snow(T,I):
    m = len(T)
    n = len(I)
    tab = [0 for _ in range(m)]
    for i in range(n):
        for j in range(I[i][0],I[i][1]+1):
            tab[j] += 1
    return max(tab)
"""
idea:
brut jest n * m

brute force na pałe, dla każdego dnia dodajemy śnieg na miejsca na autostradzie gdzie potrzeba
liniowo by się dało tak jak te kwadraty z maksymalnym przecięciem? - chyba ciężko ze zliczaniem


"""

"""
idea na wzorcówkę:
zamieniamy przedziały na krotki postaci (liczba, 0/1 zależnie od tego czy początek/koniec przedziału)
"""

def snow(T,I):
    n = len(I)
    I_new = []
    for i in range(n):
        I_new.append((I[i][0],0))
        I_new.append((I[i][1], 1))
    I_new.sort(key = lambda x: (x[0],x[1]))
    counter = 0
    maxi = 0
    for i in range(2*n):
        if I_new[i][1] == 0:
            counter += 1
        else:
            counter -=1
        if counter > maxi:
            maxi = counter
    return maxi

I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
T = 100
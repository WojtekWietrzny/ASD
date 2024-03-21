"""
napisać funkcję, która sprawda czy 2 słowa będą anagramami
a) a - z ( bez ą)
b) dowolne znaki (21 - bit)
"""

#import NumPy

#opcja a
def anagram_a(a,b): #ord to funkcja przypisujaca znakowi wartosc kodu / zamienia na liczbe
    z_code = ord("z") # kody znaków alfabetu zwykłęgo są koło siebie
    a_code = ord("a")
    na = len(a)
    nb = len(b)
    if na != nb:
        return False
    count_table_a = [0] * (z_code - a_code + 1)
    count_table_b = [0] * (z_code - a_code + 1)
    for i in range(na):
        count_table_a[ord(a[i]) - a_code] += 1
        count_table_b[ord(b[i]) - a_code] += 1
    return count_table_a == count_table_b
    # możnaby zrobić z jedną tablicą count, wtedy przy a dodajemy z indeksu, a przy b odejmujemy z indeksu
# powyższe rozwiązanie jest dla alfabetu, złożoność obliczeniowa to O(24 + n)
def anagram_one_tab_a(a,b): #ord to funkcja przypisujaca znakowi wartosc kodu / zamienia na liczbe
    z_code = ord("z") # kody znaków alfabetu zwykłęgo są koło siebie
    a_code = ord("a")
    na = len(a)
    nb = len(b)
    if na != nb:
        return False
    count_table = [0] * (z_code - a_code + 1)
    for i in range(na):
        count_table[ord(a[i]) - a_code] += 1
        count_table[ord(b[i]) - a_code] -= 1
    return count_table_a == count_table_b
"""
w numpy jest funkcja numpy.empty(24 (albo 2^21)) i ona alokuje tablice o takiej długości
tylko ona nie będzie zerowana
"""
# opcja b - tablica tab ma 2 miliony elementów około
def anagram_one_tab_b(a,b):
     tab = numpy.empty(2^21)
     na = len(a)
     nb = len(b)
     if na != nb:
         return False
     for i in range(na):
         tab[ord(a[i])] = 0
         tab[ord(b[i])] = 0
     for i in range(na):
         tab[ord(a[i])] += 1
         tab[ord(b[i])] -= 1
     for i in range(na):
         if tab[ord(a[i])] != 0 or tab[ord(b[i])] != 0: # możn sprawdzać tylko jedno
             return False
     return True

print(anagram_one_tab_b('2#$%@&^*(','#$%@&*^2'))


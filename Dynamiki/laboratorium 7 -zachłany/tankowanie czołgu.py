"""
Zadanie 1. (problem stacji benzynowych) Czołg jedzie z punktu A do punktu B. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A do B to prosta, na której znajdują się stacje benzynowe (na pozycjach będących liczbami naturalnymi; A jest na pozycji 0). Proszę podać algorytmy dla następujących przypadków:
(1) Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna.
(2) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodat- kowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
(3) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna.
"""

"""
T - odległości i-tych stacji od początku

"""


def get_station_idx(S: 'array with distances of stations from the starting point',
                    l: 'begin index of a subarray',
                    r: 'end index of a subarray',
                    R: 'the most distant point a tank can reach'):
    while l <= r:
        mid = (l + r) // 2
        if R < S[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return r





def fuelling(L,S,t,fuel) # L - pojemność baku, S - odległości stacji od początku, T - długość do przejechania, fuel - ilość paliwa na początku
    if fuel >= t:
        return 0
    if S[0] > fuel:
        return -1
    first_station_index = get_station_idx(S,0,len(S) - 1, fuel)
    last_station_index = get_station_idx(S,)
"""
idea:
liniowo tablica tak, żeby były krotki (mniejsze, większe)
sortujemy po [1], potem po [0]
zmiana danych, żeby nie było O(o w chuj długość tablicy)
dp[i] - największa liczba przedziałów nie przecinających się do indeksu i-tego
dp[i] = max(dp[i],1 + dp[początek rozważanego przedziału])
"""

"""

t = [krańce przedziałów] * 2n
sort...... - rosnąco
for i in range( 2 *n):
    t[i] = (t[i] - klucz,i - wartosc)
    tablica krotek - 
wrzucamy do słownika
dla kazdego przedziału, szukamy klucza lewego krańca, przypisujemy mu wartość
to samo dla prawego, nadpisujemy całą krotkę
potem algorytm jest nlogn
"""

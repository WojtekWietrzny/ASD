"""
napisać algorytm, który sortuje n - elementową tablicę
zawierającą liczby z zakresu 0,1,2,3,...., n^2-1
używamy counting sorta, na danych, które sobie wcześniej przygotowaliśmy
zależy nam na stabilności
"""

def sort(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i] % n, T[i] // n)
    def sort_2(T,x):
        


        k = [0 for _ in range(n)]
        for i in range(n):
            k[T[i][0]] += 1
        for i in range(n):
            k[i] += k[i-1]


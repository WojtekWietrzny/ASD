"""
Proszę opisać (bez implementacji!) jak najszybszy algorytm, który otrzymuje na wejściu pewien
ciąg n liter oraz liczbę k i wypisuje najczęściej powtarzający się podciąg długości k (jeśli ciągów
mogących stanowić rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że
ciąg składa się wyłącznie z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k = 3 rozwiązaniem jest zarówno ciąg aba, który
powtarza się dwa razy (to, że te wystąpienia na siebie nachodzą nie jest istotne). Zaproponowany
algorytm opisać, uzasadnić jego poprawność oraz oszacować jego złożoność.
"""
def counting_sort(A,k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1,k):
        C[i] += C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]

def radix_sort(tab,k):
    n = len(tab)
    for i in range(k-1,-1,-1):
        A = []
        B = []
        for j in range(n):
            if tab[j][i] == "a":
                A.append(tab[j])
            elif tab[j][i] == "b":
                B.append(tab[j])
        tab = A + B
        print(tab)
    return tab
def k_ciag(arr,k):
    n = len(arr)
    tab_ciag = []
    for i in range(n-k):
        s = arr[i:i+k]
        tab_ciag.append(s)
    T = radix_sort(tab_ciag,k)
    counter = 1
    maxi = 0
    for i in range(1,n-k):
        if T[i-1] == T[i]:
            counter += 1
        else:
            if counter > maxi:
                maxi = counter
            counter = 0
    return maxi
slowo = 'ababaaaabb'
print(k_ciag(slowo,3))

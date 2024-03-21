"""
Zadanie 3. (ładowanie przyczepy) Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków o wagach w1,...,
wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład,
dla siedmiu ładunków wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27).
Proszę podać algorytm zachłanny (i uzasadnić jego poprawność), który wybiera ładunki tak,
że przyczepa jest możliwie maksymalnie zapełniona (ale bez przekraczania pojemności) i
jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się np. załadować przyczepę
do pełna uzywając 100 ładunków, albo zaladować do pojemności K – 1 używając jednego ładunku,
to lepsze jest to pierwsze rozwiązanie).
"""

def fill_the_trailer(W,k):
    n = len(W)
    W.sort(reverse = True)
    result = []
    for w in W:
        if w <= k:
            k -= w
            result.append(w)
    return result

W = [2, 2, 4, 8, 1, 8, 16]
k = 27

print(fill_the_trailer(W, k))
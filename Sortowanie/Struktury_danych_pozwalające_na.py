"""
zadanie 1
Zaproponować strukturę danych, która pozwala na:
- Insert
- Remove max
- Remove min
każda z tych funkcji ma działać w O(logn)
zadanie 2
ma dawać:
- Insert
- Remove Median
"""

"""
zadanie 1
to są dwa kopce, jeden zrobiony w sposób min, drugi w sposób max
insert napisane w Heap Sorcie
remove max działa w czasie logarytmicznym, ta pierwsza wersja maćka
zamieniamy od dołu 
remove min - szukamy liści - nie da sie zrobic na jednym kopcu, trzeba zrobic 2 kopce
jezeli to jest lisc to zamieniamy z ostatnim elementem 
jezeli to nie jest lisc to zamieni
"""

"""
usuwanie z góry kopca - np. max - wstawiamy jakiś element z dołu za niego i porównujemy z synami
jeśli jest mniejszy od obu to zamieniamy z wiekszym i powtarzamy
w innym przypadku zamieniamy z tym od którego jest mniejszy
usuwanie z góry
"""


"""
zadanie 2
budowanie kopca - budujemy normalnie - mniejsze od mediany do lewego kopca, wieksze do prawego
jesli roznica bedzie wieksza od 1 to trzeba zbalansowac, gorny przerzucamy na lewo albo na prawo i reszta sie dopasowuje
usuwanie mediany - bierzemy element środkowy, po jego lewej stronie jest (n-1)/2, po jego prawej tyle samo
chcemy mieć 2 kopce, jeden max, drugi min
w lewym bedzie n//2, a w prawym n-1//2 (jesli nieparzyscie to mediana jest najwyzszy w lewym,
jesli parzyscie to srednia arytmetyczna gornych 
chcemy żeby w lewym kopcu (max) było o jeden więcej albo tyle samo
jesli w lewym jest wiecej to mediana jest na gorze w lewym
jesli tyle samo to srednia arytmetyczna dwoch gornych
zawsze po dodaniu roznica ilosci elementow musi byc maksymalnie 1, jesli nie to to co na gorze
w max np. największy będzie 15, w min najmniejszy 20
"""
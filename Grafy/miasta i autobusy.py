"""
zadanie:
jeździmy autobusami po mieście
graf zadany jest w ten sposób
mamy podane podane miasto a z którego jedziremy, miasto b do którego jedziemy i c przepustowość autobusu - tak jest
opisana każda krawędź

pomysl:
coś jakby algorytm Daikstry, w którym mamy najmniejszą możliwą pojemność tych
pomysł 2:
działamy na binsearchu - szzukamy największej z najmniejszych ilości osób w grupie, dla których
dopuszczalna złożonośc:
liczba trójek * logarytm z największej wagi (największej pojemności autobusu) - często robiony trik na kolokwium
logarytm z pojemności sugeruje wyszukiwanie binarne - wtedy wiemy że sprawdzanie musi być liniowe - to zrobimy z BFS
"""
"""
zadanie:
mamy zbiór walut - reprezentowany w macierzy
K[x][y] - ile trzeba zaplacic w walucie x za jedna jednostke waluty y
efektywnie po prostu tablica kursów wymiany walut
chcemy upewnić się, że nie ma żadnego cyklu w którym robiąc ileś wymian dostaniemy więcej waluty a niż pierwotnie
"""
"""
pomysł
K[x][y] - za 1 jednostkę x dostajemy ileś jednostek y
mnożymy sobie K[X1][X2] * k[X2][X3] *.....* k[XN][X1] > 1 - JEŚLI TO JEST SPEŁNIONE TO MOŻNA ZAROBIĆ 
chcemy zamienić iloczyn na sumy
logarytmujemy obie strony i mamy 
log K[X1][X2] + log k[X2][X3] +.....+ log k[XN][X1] > 0
mnożymy razy -1, bo umiemy znajdować tylko cykle o ujemnej sumie wag
-log K[X1][X2] - log k[X2][X3] -.....- log k[XN][X1] < 0
mamy nowy graf ważony z tymi ujemnymi logarytmami jako wagami
w tym grafie szukamy cykli o ujemnej sumie
puszczamy algorymt bellmana forda
n razy on wykonuje relaksacje
iterujemy po kazdym jeszcze raz po kazdym i sprawdzamy czy można wykonać relaksacje (dobrze to zapisałem?)
"""
"""
za pomocą 3/2 n porównań chcemy znależć maksimum i minimum w tablicy n elemenetowej
algorytm : porównujemy pary, mniejszą z pary porównujemy z minimum, większą z maksimum, ewentualnie zamieniamy kiedy potrzeba
np. dla [2,4,6,8]
2 z 4
2 to minimum
4 to maksimum
6 z 8
6 porownujemy z minimum - 2, wieksze wiec nie zmieniamy
8 porownujemy z maksimum - 6, wieksze wiec zmieniamy
3/2 razy n (czyli 4) to 6, więc się zgadza
"""
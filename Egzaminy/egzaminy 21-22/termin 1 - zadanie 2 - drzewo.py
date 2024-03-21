"""
idea:
używamy BFS - zapisujemy pewien czas przetworzenia w tablicy dla kazdego poziomu
potem robimy tablice o dlugosci najwiekszy czas przetworzenia +1 i
przechodzimy po calym grafie zapisujac +1 do indeksu poziomu wierzcholka na ktorym sie znajdujemy
potem bierzemy najnizszy poziom na ktorym jest max lisci, bo chcemy miec najwyzsze drzewo a wszystkie maja ten sam korzen
usuwamy wszystko pomiedzy naszym wybranym poziomem a kolejnym
wracamy sie po parentach z kazdego liscia, usuwamy syna, drugiego niz ten z ktorego przychodzimy, jesli istnieje
"""
"""
mamy dużo pojemników 2 wymiarowych
lewy górny róg ma współrzędne (p,q), prawy dolny (u,v)
system takich pojemników jest połączony rurkami, nie mającymi pojemności, tylko długość
każda rurka jest podpięta od dołu do danego pojemnika
musimy odpowiedzieć ile pojemników jesteśmy w stanie zapełnić przy danej liczbie litrów
"""

"""
rozwiązanie:
mamy 2 listy krotek, jedna okreslajaca dolne krawedzie, druga gorne
to będą listy zawierające 2 elementowe krotki - wysokość i szerokości
sortujemy je rosnaco, jedna po wysokosciach, druga po szerokosciach
szukam wysokosci, sprawdzam co jest dla niej zapelnione, co czesciowo zapelnione, dodaje 
jeśli objetosc za duzo to wysokosc strzelam w jej polowise w dol
jesli za mala to w polowie tego co zostało u góry
"""
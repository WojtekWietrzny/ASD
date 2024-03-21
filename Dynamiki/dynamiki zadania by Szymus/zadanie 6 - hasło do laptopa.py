"""
idea:
patrzymy na to zadanie jak na ciągi rekurencyjne z dyskretnej
jeśli mamy na początku 0 to liczba jest nieprawidłowa
jeśli pojawia się zero i nie jest poprzedzone jedynką lub dwójką to też jest nieprawidłowe
jeśli dodamy się coś róznego od 0 i jest poprzedzone 0 to mamy tyle samo ciągów co przed jej dodaniem
jeśli nasze 2 ostatnie cyfry dają liczbę mniejszą niż 27 i większą lub równą 10, to znaczy że możemy dodać albo literę dwucyfrową
albo jednocyfrową

złożoność czasowa:
O(n)
złożoność pamięciowa:
O(n)
"""


def password(T):
    n = len(T)
    dp = [0 for _ in range(n)]
    if int(T[0]) == 0:
        return 0
    dp[0] = 1
    if int(T[0:2]) < 27:
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2,n):
        if int(T[i]) == 0:
            if int(T[i-1]) != 1 and int(T[i-1]) != 2:
                return 0
            else:
                dp[i] = dp[i-2]
        elif int(T[i]) != 0 and int(T[i-1] == 0):
            dp[i] = dp[i-1]
        elif int(T[i-1:i+1]) <= 26 and int(T[i-1:i+1]) >= 10:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]

    return dp[n-1]


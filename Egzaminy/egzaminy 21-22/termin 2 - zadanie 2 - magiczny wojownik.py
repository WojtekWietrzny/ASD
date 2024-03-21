"""
idea na akceptowalną:
dp[i] - maksymalna ilość sztabek złota, którą możemy osiągnąć przed wejściem na i-ty indeks
przechodzimy po każdej komnacie
sprawdzamy dla każdej komnaty drzwi prowadzące do innych
chcemy zawsze brać
"""

def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        if dp[i] == -1: # nie da się dojść do pola i
            continue
        for j in range(1, 4):
            if C[i][j][1] == -1: #drzwi prowadzą do nikąd
                continue
            for k in range(11):
                if C[i][j][0] == C[i][0] - k: # bierzemy maksymalną ilość
                    dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + k)
                elif C[i][j][0] > C[i][0] - k:
                    break
            if C[i][0] < C[i][j][0] and dp[i] + C[i][0] - C[i][j][0] >= 0: #kasa ze skrzyni nie wystarcza na opłacenie drzwi
                dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + C[i][0] - C[i][j][0]) #ale dokładamy wystarczająco z kieszeni
    return dp[n - 1]





















#nowe podejście

def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n): # iterujemy po wszystkich komnatach
        if dp[i] == -1: # nie da się dojść
            continue
        for j in range(1,4): # iterujemy po drzwiach
            if C[i][j][1] == -1:
                continue
            for k in range(11): # iterujemy po ilości branych monet z komnaty
                if C[i][j][0] == C[i][0] - k:
                    dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + k)
                elif C[i][j][0] > C[i][0] - k:
                    break
            if C[i][0] < C[i][j][0] and dp[i] + C[i][0] - C[i][j][0] >= 0:  # kasa ze skrzyni nie wystarcza na opłacenie drzwi
                dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + C[i][0] - C[i][j][0])
    return dp[n-1]


















"""
idea:
iterujemy po wszystkich komnatach
iterujemy po wszystkich drzwiach
iterujem
"""

def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n): # iteracja po wszystkich pokojach
        if dp[i] == -1: #nie można wejść do danej komnaty
            continue
        for j in range(1,4):
            if C[i][j][1] == -1:
                continue
            for k in range(11):
                if C[i][j][0] == C[i][0] - k: # bierzemy maksa
                    dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i]+k)
                elif C[i][j][0] > C[i][0] - k: # za duży koszt wejścia
                    break
            if C[i][j][0] > C[i][0] - k and C[i][j][0] <= dp[i] + C[i][0]:
                dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] - C[i][j][0] + C[i][0])
    return dp[n-1]


















"""
idea na akceptowalną:
dp[i] - maksymalna ilość sztabek złota, którą możemy osiągnąć przed wejściem na i-ty indeks
przechodzimy po każdej komnacie
sprawdzamy dla każdej komnaty drzwi prowadzące do innych
chcemy zawsze brać
"""

def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for i in range(n): # iteruje po komnatach
        if dp[i] == -1:
            break
        for j in range(1,4): # sprawdzam każde drzwi
            if C[i][j][1] == -1:
                break
            for k in range(11): # k to ilość monet które biorę, moge wziąć max 10
                if k == C[i][0] - C[i][j][0]: # bierzemy maksimum ile możemy po opłaceniu kosztu
                    dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + k)
                elif k > C[i][0] - C[i][j][0]: # za duży koszt wejścia
                    break
            if k > C[i][0] - C[i][j][0] and C[i][j][0] - C[i][0] <= dp[i]:
                dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] - C[i][j][0] + C[i][0])
    return dp[n-1]


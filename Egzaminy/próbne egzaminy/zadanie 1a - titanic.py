"""
idea:
robie tablice dynamiczną długości wszystkich użytych znaków w zapisie morse'a
dp[i] - oznacza minimalną ilość liter użytą do zakodowania kodu do i-tego elementu włącznie
iterujemy po każdej literze
w tej pętli dodatkowo iterujemy po każdej literze z listy D
jeśli równa się z tym co mamy w kodzie cofając się odpowiednią liczbę znaków do tyłu
to bierzemy na dp[i] min(dp[i], dp[i - len(litera)] + 1
"""


def titanic(W, M, D): # złożoność n * m
    inf = float('inf')
    morse = ""
    for i in range(len(W)):
        letter = W[i]
        morse = morse + M[ord(letter) - 65][1]
    n = len(morse)
    m = len(D)
    dp = [inf for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(1,n + 1):
        for j in range(m):
            if M[D[j]][1] == morse[i - len(M[D[j]][1]) + 1 :i + 1]:
                dp[i + 1] = min(dp[i + 1], dp[i + 1 - len(M[D[j]][1])] + 1)

    return dp[n]
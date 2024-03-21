def knapsack2D(P: 'array of profits',
               H: 'array of heights',
               W: 'array of weights',
               MaxH: 'max total height of items',
               MaxW: 'max total weight of items'
               ):
    n = len(P)
    H, W = filter_items(H, W, MaxH, MaxW)
    # Create an array for caching values
    F = create_arr(n, MaxH + 1, MaxW + 1)

    for h in range(H[0], MaxH + 1):
        for w in range(W[0], MaxW + 1):
            F[0][h][w] = P[0]

    for i in range(1, n):
        for h in range(1, MaxH + 1):
            for w in range(1, MaxW + 1):
                F[i][h][w] = F[i - 1][h][w]

                if H[i] <= h and W[i] <= w:
                    F[i][h][w] = max(F[i][h][w], F[i - 1][h - H[i]][w - W[i]] + P[i])

    print_F(F)

    return F[n - 1][MaxH][MaxW]
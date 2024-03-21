def ogrod(S, V): #złożoność n^2
    n = len(S)
    m = len(V)
    sum = 0
    max_sum = 0

    for i in range(n):
        types = [0 for _ in range(m)]
        sum = 0
        for j in range(i, n):
            if types[S[j]-1] == 0:
                types[S[j]-1] += 1
                sum += V[S[j]-1]
                if sum > max_sum:
                    max_sum = sum
                    print(types)
                    print(max_sum)
            elif types[S[j]-1] == 1:
                types[S[j]-1] += 1
                sum -= V[S[j]-1]
            else:
                continue
    return max_sum

S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V = [5, 3, 6, 6]

print(ogrod(S, V))

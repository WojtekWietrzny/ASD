def lamps(n,L):
    n = len(I)
    tab = [0 for _ in range(n)]
    for i in range(n):
        L_new.append((L[i][0],0))
        I_new.append((L[i][1], 1))
    L_new.sort(key = lambda x: (x[0],x[1]))
    counter = 0
    maxi = 0
    for i in range(2*n):
        if I_new[i][1] == 0:
            counter += 1
        else:
            counter -=1
        if counter > maxi:
            maxi = counter
    return maxi
# kod ze śniegu, jednak nie idzie podobnie

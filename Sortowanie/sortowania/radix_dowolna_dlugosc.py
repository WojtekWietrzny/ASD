def counting_sort(x):
    code_a = ord("a")
    n=len(x)
    B=[0]*n
    C=[0]*26

    for i in range(n):
        C[ord(x[i])-code_a]+=1

    for i in range(1,26):
        C[i]=C[i-1]+C[i]

    for i in range(n-1,-1,-1):
        B[C[ord(x[i])-code_a]-1]=x[i]
        C[ord(x[i])-code_a]-=1

    return B

def radix_sort(T, index):
    a_code = ord("a")
    while index >= 0:
        C = [[] for i in range(27)]

        for i in range(len(T)):
            if len(T[i]) <= index:
                C[26] += [T[i]]

            else:
                C[ord(T[i][index]) - code_a] += [T[i]]

        B = []
        for bucket in C:
            B += bucket

        T = B.copy()
        index -= 1

    return T

#def sort()
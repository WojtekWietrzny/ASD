def insertion_sort(T,p,r):
    for i in range(p+1,r+1):
        x=i
        y=i-1
        while y>=p and T[x]<T[y]:
            T[x],T[y] =T[y],T[x]
            x-=1
            y-=1

def magic_fives(T,p,r):
    n=len(T)
    if len(T)==1:
        return T[0]

    A=[]
    for i in range(0,r,5):
        if i>r-4:
            insertion_sort(T,i,r)
            A.append(T[(r+i)//2])
        else:
            insertion_sort(T,i,i+5)
            A.append(T[i+2])
    n=len(A)
    print(A)
    return magic_fives(A,0,n-1)


print(magic_fives([40,12,45,32,33,55,22],0,6))
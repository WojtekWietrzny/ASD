# n porownan dla posortowanej, gdy k elementow na zlej pozycji to O(k*n)
def insertion_sort(T):
    for i in range(1,len(T)):
        y=i-1
        x=i
        while y>=0 and T[x]<T[y]:
            T[x],T[y] = T[y],T[x]
            x-=1
            y-=1

T=[2,8,1,4,5,6,3]
insertion_sort(T)
print(T)
"""# Bucket Sort in Python

def bucketSort(array):
    bucket = [0]
    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array"""

def insertion_sort(T):
    for i in range(1,len(T)):
        y=i-1
        x=i
        while y>=0 and T[x]<T[y]:
            T[x],T[y] = T[y],T[x]
            x-=1
            y-=1

def bucket_sort(T):  # rozkład jednostajny, el nalezy do <0,1) wymierne
    n = len(T)
    A = [[] for i in range(n)]  # bucket0 <0,1/n)

    for i in range(n):
        A[int(T[i] * n)].append(T[i])

    for bucket in A:
        insertion_sort(bucket)

    i = 0

    for bucket in A:
        for el in bucket:
            T[i] = el
            i += 1


T = [0.24, 0.51, 0.10, 0.55]
bucket_sort(T)
print(T)
"""array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))
"""
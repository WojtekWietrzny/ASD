"""# Radix sort in Python
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)
"""

# sortowanie pozycyjne
# ord(k) = 107
# chr(107 = k

def counting_sort(A, p, k, x):
    n = len(A)
    C = [0]*(k-p+1)
    B = [0]*n
    for i in range(n):  # ile razy wystepuje liczba rowna danej
        C[ord(A[i][x]) - p] += 1
    for j in range(1, k-p+1):  # ile razy wystepuje liczba mniejsza lub rowna danej
            C[j] = C[j] + C[j-1]
    for i in range(n-1,-1,-1):
        B[C[ord(A[i][x]) - p]-1] = A[i]
        C[ord(A[i][x]) - p] -= 1

    for i in range(n):
        A[i] = B[i]
    return A


def radix_sort(T):
    n = len(T)
    k = len(T[0])
    for i in range(k-1,-1,-1):
        counting_sort(T, ord("a"), ord("z"), i)
    return(T)


print(ord("a"), ord("z"))
T = ["kra", "art", "kot", "kit", "ati", "kil"]
print(radix_sort(T))
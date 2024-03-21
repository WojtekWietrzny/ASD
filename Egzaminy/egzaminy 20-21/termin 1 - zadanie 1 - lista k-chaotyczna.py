def chaos_index(T):
    n = len(T)
    def merge_altered(T, p, q, r, key):
        L = T[p:q + 1]
        R = T[q + 1:r + 1]

        L += [tuple('inf')]
        R += [tuple('inf')]

        i = 0  # iterator L
        j = 0  # iterator R

        for k in range(r - p + 1):
            if L[i][key] <= R[j][key]:
                T[p + k] = L[i]
                i += 1

            else:
                T[p + k] = R[j]
                j += 1

    def merge_sort_altered(arr, key):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_altered(left, key)
        merge_sort_altered(right, key)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][key] <= right[j][key]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr
    for i in range(n):
        T[i] = (T[i],i)
    merge_sort_altered(T,0)

    k = 0
    for i in range(n):
        k = max(k,abs(i - T[i][1]))
    return k
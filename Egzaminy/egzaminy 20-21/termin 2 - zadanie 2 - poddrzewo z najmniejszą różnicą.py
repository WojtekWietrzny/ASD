def balance(A):
    def recur_len(counter,A):
        if A.edges.empty():
            return 1
        for element in A.edges:
            counter += recur_len(counter,element)
        return counter + 1

    def recur_sum(i, )
    n = recur_len(0,A)
    Sum = [0 for _ in range(n)]

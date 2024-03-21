def jobs(T): #deadline, profit
    n = len(T)
    limit = 0
    T.sort(reverse=True, key=lambda x: x[1])
    for i in range(n):
        if limit < T[i][0]:
            limit = T[i][0]
    slots = [0 for _ in range(limit+1)]
    for task in T:
        for i in range(task[0], -1, -1):
            if slots[i] == 0:
                slots[i] = task
                break
    return slots







T = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15]
]
print(jobs(T))
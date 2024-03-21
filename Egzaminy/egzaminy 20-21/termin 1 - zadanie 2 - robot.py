from queue import PriorityQueue


"""def robot(L, A, B):
    DP = [[[[-1] * 3 for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    queue = PriorityQueue()
    queue.put((0, A[0], A[1], 0, 0))
    possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    seconds = [60, 40, 30]
    while not queue.empty():
        time, x, y, direction, idx = queue.get()
        if (x, y) == B:
            return time
        if DP[y][x][direction][idx] != -1 or L[y][x] == 'X':
            continue
        DP[y][x][direction][idx] = time
        queue.put((time + 45, x, y, (direction + 1) % 4, 0))
        queue.put((time + 45, x, y, (direction + 3) % 4, 0))
        x += possible_moves[direction][0]
        y += possible_moves[direction][1]
        queue.put((time + seconds[idx], x, y, direction, min(idx + 1, 2)))"""






























def robot(L, A, B):
    n = len(L)
    m = len(L[0])
    queue = PriorityQueue()
    dp = [[[-1 for i in range(4)] for _ in range(m)] for _ in range(n)]
    x = A[0]
    y = A[1]
    queue.put((0, x, y, 0, 0))  # czas, polozenie, prawo, (0,1,2,3 - konkretne kierunki), ile ruchow do przodu za nami

    while not queue.empty():
        time, X, Y, turn, move = queue.get()
        if dp[Y][X][turn]!= -1:
            dp[Y][X][turn] = time

        if X == B[0] and Y == B[1]:
            return time

        if move == 0:
            add_time = 60
        elif move == 1:
            add_time = 40
        else:
            add_time = 30

        if turn == 0 and X + 1 <= m - 1 and L[Y][X + 1] != 'X':
            queue.put((time + add_time, X + 1, Y, turn, move + 1))
        elif turn == 1 and Y + 1 <= n - 1 and L[Y + 1][X] != 'X':
            queue.put((time + add_time, X, Y + 1, turn, move + 1))
        elif turn == 2 and X - 1 >= 0 and L[Y][X - 1] != 'X':
            queue.put((time + add_time, X - 1, Y, turn, move + 1))
        elif turn == 3 and Y - 1 >= 0 and L[Y - 1][X] != 'X':
            queue.put((time + add_time, X, Y - 1, turn, move + 1))

        if dp[Y][X][(turn + 1) % 4] == -1:
            queue.put((time + 45, X, Y, (turn + 1) % 4, 0))  # obrót w prawo

        if dp[Y][X][(turn -1) % 4] == -1:
            queue.put((time + 45, X, Y, (turn - 1) % 4, 0))  # obrót w lewo



L = [ "XXXXXXXXXX", # 0
      "X X      X", # 1
      "X XXXXXX X", # 2
      "X        X", # 3
      "XXXXXXXXXX"] # 4
A = [1,1]
B = [8,3]
print(robot(L, A, B))



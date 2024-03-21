#TODO
def map_cars(A, L):
    total = 0
    for i in range(len(A)):
        A[i] = int(A[i] * 100 + .5)
        total += A[i]
        # If we exceeded maximum possible length, return an index of the last car
        if total > 2 * L:
            return i - 1
    # If all may fit in, return the last possible car's index
    return len(A) - 1


def ferry(L: 'length of a ferry', A: 'array of cars lengths'):
    # Map all car lengths to the integer values (multiply by 100)
    # and leave all the cars which in no way can fit in the ferry
    n = len(A)
    L = int(100 * L + .5)
    last_i = map_cars(A, L)
    # Prepare array which will be used to cache values
    F = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(last_i + 1)]
    P = [''] * n

    def recur(i: 'current car index',
              l: 'remaining space on the left lane',
              r: 'remaining space on the right lane'):
        # If the next car cannot fit in
        if l < 0 or r < 0:
            return False
        if i == 0:
            if l >= A[0]: P[0] = 'L'; return True
            if r >= A[0]: P[0] = 'R'; return True
            return False
        if F[i][l][r] is None:
            if recur(i - 1, l - A[i], r):
                F[i][l][r] = True
                P[i] = 'L'
            elif recur(i - 1, l, r - A[i]):
                F[i][l][r] = True
                P[i] = 'R'
        return F[i][l][r]

    for i in range(last_i, -1, -1):
        if recur(i, L, L):
            return i + 1, P
    return -1, []



"""
z discorda
def prom_2_way(T, r):
  dp = [False for _ in range(r+1)]
  dp[0] = True
  
  max_dp = 0
  whl_len = 0
  
  i = 0
  while r + max_dp >= whl_len  and  i < len(T):
    if T[i] > r:
      return "ERROR"
    
    for j in range(r+1):
      
      new_j = j + T[i]
      if dp[j]  and  new_j <= r:
        dp[new_j] = True
        max_dp = max(max_dp, new_j)
        
    whl_len += T[i]
    i+=1
    
  return i - (r + max_dp < whl_len)
        
    


T = [1, 3, 4, 5, 6, 1, 1, 2, 13]
r = 10
print(prom_2_way(T, r))
"""
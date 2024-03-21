def money_change(coins, ammount):
    dp = [ammount+1 for _ in range(ammount+1)]
    dp[0] = 0
    for i in range(ammount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i],dp[i-coin] + 1)

    if dp[ammount] <= ammount:
        return dp[ammount]
    else:
        return -1

coins = [2, 5]
amount = 19
print(money_change(coins, amount))

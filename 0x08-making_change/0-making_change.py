#!/usr/bin/python3


"""function that determine the fewest number of coins

"""


def makeChange(coins, total):
    """makeChange function

    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

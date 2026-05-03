# Brute Force
from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


# One-Pass (Optimal)
from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        # Update profit if selling at current price is better
        max_profit = max(max_profit, p - min_price)
        # Update min_price if we find a lower buying price
        min_price = min(min_price, p)
    return max_profit
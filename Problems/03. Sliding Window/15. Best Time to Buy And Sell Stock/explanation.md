# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Problem Link:** [LeetCode 121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

## Examples

| Input                    | Output | Explanation                                                                 |
| ------------------------ | ------ | --------------------------------------------------------------------------- |
| `prices = [7,1,5,3,6,4]` | `5`    | Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5. |
| `prices = [7,6,4,3,1]`   | `0`    | Prices only decrease; no transaction yields profit.                         |
| `prices = [1,2]`         | `1`    | Buy day 1 (1), sell day 2 (2), profit = 1.                                  |
| `prices = [2,1]`         | `0`    | No profit possible.                                                         |

## Approach

We need to find the maximum difference `prices[j] - prices[i]` where `i < j`. The naive solution checks every pair, but we can do better.

### 1. Brute Force (O(n²))

Check every possible buy and sell day combination. Computes the profit for each pair and tracks the maximum. This is too slow for large inputs.

### 2. One-Pass (Greedy, Optimal)

As we iterate through the array, we can maintain two pieces of information:

- `min_price`: the lowest price seen so far (the best day to buy up to the current day).
- `max_profit`: the maximum profit achievable if we were to sell on the current day (current price − min_price).

By updating `min_price` as we go, we guarantee that we always use a past buying price. This is O(n) time and O(1) space.

### Algorithm Steps (One-Pass)

1. Initialize `min_price = prices[0]`, `max_profit = 0`.
2. For each `price` in `prices`:
   - If `price - min_price > max_profit`, update `max_profit`.
   - If `price < min_price`, update `min_price`.
3. Return `max_profit`.

## Complexity Analysis

| Method      | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n²) | O(1)  |
| One-Pass    | O(n)  | O(1)  |

- **Time Complexity:** O(n) — single pass through the array.
- **Space Complexity:** O(1) — only two variables.

## Code (Python)

### Brute Force (for understanding)

```python
from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit
```

### One-Pass (Optimal)

```python
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
```

## Edge Cases

- **Empty array or single price:** Not possible per constraints (length ≥ 1), but code handles single element (max_profit stays 0).
- **Decreasing prices:** Returns 0 (no profit).
- **Constant prices:** All equal, profit 0.
- **Large input (up to 10⁵):** O(n) time is efficient.

## Alternative Approaches

| Approach           | Time       | Space    | Notes                                       |
| ------------------ | ---------- | -------- | ------------------------------------------- |
| Brute force        | O(n²)      | O(1)     | Too slow for large inputs.                  |
| Divide and Conquer | O(n log n) | O(log n) | Similar to maximum subarray; overkill here. |
| One-Pass (above)   | O(n)       | O(1)     | Optimal; standard solution.                 |

The one-pass method is the most efficient and is equivalent to keeping a running minimum and maximum difference.

# 167. Two Sum II – Input Array Is Sorted

**Difficulty:** Medium  
**Problem Link:** [LeetCode 167 - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return _the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2._

The tests are generated such that there is **exactly one solution**. You may not use the same element twice.

Your solution must use only **constant extra space**.

## Examples

| Input                                 | Output  | Explanation                     |
| ------------------------------------- | ------- | ------------------------------- |
| `numbers = [2,7,11,15]`, `target = 9` | `[1,2]` | `2 + 7 = 9`, indices 1 and 2.   |
| `numbers = [2,3,4]`, `target = 6`     | `[1,3]` | `2 + 4 = 6`, indices 1 and 3.   |
| `numbers = [-1,0]`, `target = -1`     | `[1,2]` | `-1 + 0 = -1`, indices 1 and 2. |

## Approach

We exploit the fact that the input array is **sorted**. The **two‑pointer technique** gives an O(n) time, O(1) space solution.

### Why Two Pointers?

- Start one pointer (`left`) at the beginning (smallest element) and another (`right`) at the end (largest element).
- Compute the sum `curr = numbers[left] + numbers[right]`.
- If `curr == target`, we have found the solution.
- If `curr < target`, we need a larger sum, so move `left` forward to increase the sum.
- If `curr > target`, we need a smaller sum, so move `right` backward to decrease the sum.
- Because the array is sorted, this process is guaranteed to find the unique pair without missing it.

### Algorithm Steps

1. Initialize `left = 0`, `right = len(numbers) - 1`.
2. While `left < right`:
   - `curr = numbers[left] + numbers[right]`
   - If `curr == target`: return `[left + 1, right + 1]` (convert to 1‑indexed).
   - Else if `curr < target`: `left += 1`
   - Else: `right -= 1`
3. (The problem guarantees a solution, so we will always return inside the loop.)

## Complexity Analysis

- **Time Complexity:** O(n)  
  Each element is visited at most once as the pointers move inward.
- **Space Complexity:** O(1)  
  Only a few integer variables are used.

## Code (Python)

```python
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return [left + 1, right + 1]   # 1‑indexed
        elif curr < target:
            left += 1
        else:
            right -= 1
    # According to the problem, a solution always exists
    return []
```

## Edge Cases

- **Negative numbers:** Works naturally; the sorted property still holds (e.g., `[-5, -3, 0, 1, 2]`).
- **Target composed of two identical numbers?** The problem guarantees exactly one solution, and if duplicate values form the pair, they’ll be at distinct indices (e.g., `[2,2]`, target 4 → pointers will meet them).
- **Larger target than the max sum?** The algorithm will converge; guaranteed solution exists.
- **Empty or single element array?** Not expected by constraints (length ≥ 2).

## Alternative Approaches

| Approach                     | Time       | Space | Notes                                                                         |
| ---------------------------- | ---------- | ----- | ----------------------------------------------------------------------------- |
| Brute force (nested loops)   | O(n²)      | O(1)  | Simple, but too slow for large inputs.                                        |
| Hash map (like Two Sum I)    | O(n)       | O(n)  | Works but does not exploit sorted property; uses extra space.                 |
| Binary search for complement | O(n log n) | O(1)  | For each element, binary-search the complement; still okay but slower.        |
| Two pointers (above)         | O(n)       | O(1)  | **Optimal:** exploits sorted order to achieve linear time and constant space. |

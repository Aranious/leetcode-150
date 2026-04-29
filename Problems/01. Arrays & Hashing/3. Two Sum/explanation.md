# 1. Two Sum

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1 - Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

## Examples

| Input                              | Output  | Explanation                                         |
| ---------------------------------- | ------- | --------------------------------------------------- |
| `nums = [2,7,11,15]`, `target = 9` | `[0,1]` | `nums[0] + nums[1] = 2 + 7 = 9`                     |
| `nums = [3,2,4]`, `target = 6`     | `[1,2]` | `nums[1] + nums[2] = 2 + 4 = 6`                     |
| `nums = [3,3]`, `target = 6`       | `[0,1]` | The two 3's are distinct elements, indices 0 and 1. |

## Approach

We use a **Hash Map** (dictionary) to achieve O(n) time complexity.

### Why a Hash Map?

- We need to find two numbers `a` and `b` such that `a + b = target`. This is equivalent to checking if `target - a` exists in the array.
- A hash map can store previously seen numbers and their indices. For each number `num`, we check if its complement (`target - num`) has already been seen.
- Hash map provides O(1) average-time complexity for `lookup` and `insert` operations.

### Algorithm Steps

1. Initialize an empty dictionary `num_to_index` to map each number to its index.
2. Iterate through the array using index `i` and value `num`:
   - Compute `complement = target - num`.
   - If `complement` already exists in `num_to_index`, a pair is found. Return `[num_to_index[complement], i]`.
   - Otherwise, store the current number with its index: `num_to_index[num] = i`.
3. The problem guarantees a solution, so the loop will always return. A fallback `return []` is used for completeness.

## Complexity Analysis

- **Time Complexity:** O(n)  
  We traverse the array once, and each dictionary lookup/insert is O(1) on average.
- **Space Complexity:** O(n)  
  In the worst case, we might store up to `n` elements in the hash map before finding the solution.

## Code (Python)

```python
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    # According to the problem, exactly one solution always exists,
    # so the function will always return inside the loop.
    return []
```

## Edge Cases

- Duplicate values that together form the target (e.g., `[3,3]` target `6`) → hash map correctly handles index separation.
- Negative numbers in the array or negative target → the complement logic still works.
- Large array (up to 10⁴ elements) → O(n) solution is efficient.
- Exactly one valid pair always exists, no need to handle no-solution cases (though the code includes a safe `return []`).

## Alternative Approaches

| Approach                   | Time       | Space | Notes                                                                          |
| -------------------------- | ---------- | ----- | ------------------------------------------------------------------------------ |
| Brute force (nested loops) | O(n²)      | O(1)  | Check all pairs. Too slow for large inputs.                                    |
| Two-pass hash map          | O(n)       | O(n)  | First pass builds the map, second pass looks up complements. Still O(n) time.  |
| One-pass hash map (above)  | O(n)       | O(n)  | Checks complement while building the map; slightly more efficient and concise. |
| Sorting + two-pointers     | O(n log n) | O(n)  | Requires storing original indices if sort is needed; often overkill here.      |

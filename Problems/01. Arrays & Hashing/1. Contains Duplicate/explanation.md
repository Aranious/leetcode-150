# 1. Contains Duplicate

**Difficulty:** Easy  
**Problem Link:** [LeetCode 217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Examples

| Input                          | Output  | Explanation                   |
| ------------------------------ | ------- | ----------------------------- |
| `nums = [1,2,3,1]`             | `true`  | 1 appears twice.              |
| `nums = [1,2,3,4]`             | `false` | All elements are distinct.    |
| `nums = [1,1,1,3,3,4,3,2,4,2]` | `true`  | Many duplicates.              |
| `nums = []`                    | `false` | No elements, so no duplicate. |
| `nums = [5]`                   | `false` | Single element, no duplicate. |

## Approach

We use a **Hash Set** to achieve O(n) time complexity.

### Why a Set?

- A set stores unique elements and offers O(1) average-time complexity for `add` and `contains` operations.
- We only need to remember which elements we have already seen.

### Algorithm Steps

1. Create an empty hash set `seen`.
2. Iterate through each number `num` in the input array `nums`:
   - If `num` is already in `seen` → a duplicate exists → return `true`.
   - Otherwise, add `num` to `seen`.
3. If the loop finishes without finding any duplicate → return `false`.

## Complexity Analysis

- **Time Complexity:** O(n)  
  We traverse the array once, and each set operation (insert/lookup) is O(1) on average.
- **Space Complexity:** O(n)  
  In the worst case (all elements distinct), we store all `n` elements in the set.

## Code (Python)

```python
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## Edge Cases

- Empty array → `false`
- Single element → `false`
- Array with all identical elements → `true`
- Very large array (e.g., up to 10⁵ elements) → still works in O(n) time.

## Alternative Approaches

| Approach                       | Time       | Space                          | Notes                                 |
| ------------------------------ | ---------- | ------------------------------ | ------------------------------------- |
| Brute force (nested loops)     | O(n²)      | O(1)                           | Too slow for large inputs.            |
| Sorting then checking adjacent | O(n log n) | O(1) or O(n) depending on sort | Modifies order (or uses extra space). |
| Hash Set (above)               | O(n)       | O(n)                           | Best for most cases.                  |

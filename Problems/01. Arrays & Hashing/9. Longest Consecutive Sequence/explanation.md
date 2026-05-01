# 128. Longest Consecutive Sequence

**Difficulty:** Medium  
**Problem Link:** [LeetCode 128 - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

## Examples

| Input                          | Output | Explanation                                                                     |
| ------------------------------ | ------ | ------------------------------------------------------------------------------- |
| `nums = [100,4,200,1,3,2]`     | `4`    | The longest consecutive sequence is `[1,2,3,4]`.                                |
| `nums = [0,3,7,2,5,8,4,6,0,1]` | `9`    | The longest consecutive sequence is `[0,1,2,3,4,5,6,7,8]` (duplicates ignored). |
| `nums = [1,2,0,1]`             | `3`    | Distinct values are `0,1,2` → length 3.                                         |
| `nums = []`                    | `0`    | Empty array → no sequence.                                                      |

## Approach

We need to find the longest stretch of consecutive integers, regardless of their order in the array.

### Two Main Approaches

1. **Sorting** – simple but O(n log n).
2. **Hash Set** – O(n) expected time, which meets the problem requirement.

### 1. Sorting (O(n log n))

- Sort the array.
- Iterate while keeping a current streak length.
- If `nums[i] == nums[i-1] + 1` → increment streak.
- If `nums[i] != nums[i-1]` and not consecutive → reset streak (ignore duplicates).
- Update the maximum streak along the way.

### 2. Hash Set (Optimal O(n))

The key insight: Only start counting from the **beginning** of a potential sequence. A number `num` is considered the start of a sequence only if `num - 1` is **not** in the set. Then we try to extend the sequence forward (`num+1`, `num+2`, …) as long as those numbers exist in the set.

#### Algorithm Steps (Set Method)

1. Convert the list to a set `num_set` for O(1) lookups.
2. Initialize `longest = 0`.
3. Iterate over each `num` in `num_set`:
   - If `num - 1` **not** in `num_set` → this number can start a new sequence.
   - Set `current = num`, `streak = 1`.
   - While `current + 1` is in `num_set`:
     - `current += 1`
     - `streak += 1`
   - Update `longest = max(longest, streak)`.
4. Return `longest`.

> Note: Although we have a nested `while` loop, each number is visited at most twice (once in the outer `for`, once when it's part of a sequence extending from a start). The total number of `while`-loop iterations across all starts is bounded by `n`.

## Complexity Analysis

| Method   | Time       | Space                                   |
| -------- | ---------- | --------------------------------------- |
| Sorting  | O(n log n) | O(1) (or O(n) if sort uses extra space) |
| Hash Set | O(n)       | O(n)                                    |

- **Time Complexity (Set):** O(n) – each element is processed at most twice.
- **Space Complexity (Set):** O(n) – to store all distinct numbers.

## Code (Python)

### Sorting Approach (O(n log n))

```python
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
        elif nums[i] != nums[i - 1]:  # reset streak unless duplicate
            current = 1
        longest = max(longest, current)

    return longest
```

### Hash Set Approach (Optimal O(n))

```python
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if 'num' is the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest
```

## Edge Cases

- **Empty array** → returns `0`.
- **All elements identical** (e.g., `[7,7,7,7]`) → longest streak is `1`.
- **Negative numbers** → consecutive logic works fine; `-1 - 1 = -2` is checked normally.
- **Large arrays** (up to 10⁵) → O(n) set method handles it efficiently.
- **Already sorted input** → still works; set method doesn’t rely on order.

## Alternative Approaches

| Approach                  | Time       | Space | Notes                                                                 |
| ------------------------- | ---------- | ----- | --------------------------------------------------------------------- |
| Brute force               | O(n²)      | O(1)  | For each number, check if next consecutive numbers exist by scanning. |
| Sorting (above)           | O(n log n) | O(1)  | Simple, but does not meet O(n) requirement.                           |
| Hash Set (above)          | O(n)       | O(n)  | Optimal and meets problem constraint.                                 |
| Union-Find (Disjoint Set) | O(n α(n))  | O(n)  | Overkill but doable; not straightforward.                             |

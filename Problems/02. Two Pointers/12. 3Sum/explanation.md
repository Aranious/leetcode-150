# 15. 3Sum

**Difficulty:** Medium  
**Problem Link:** [LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/)

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

Notice that the solution set must **not contain duplicate triplets**.

## Examples

| Input                     | Output                 | Explanation                                                                       |
| ------------------------- | ---------------------- | --------------------------------------------------------------------------------- |
| `nums = [-1,0,1,2,-1,-4]` | `[[-1,-1,2],[-1,0,1]]` | Two distinct triplets sum to zero. The order within each triplet does not matter. |
| `nums = [0,1,1]`          | `[]`                   | No triplet sums to 0.                                                             |
| `nums = [0,0,0]`          | `[[0,0,0]]`            | The only triplet uses the three zeros.                                            |
| `nums = [0,0,0,0]`        | `[[0,0,0]]`            | Duplicate triplets are not allowed.                                               |

## Approach

The problem asks for all unique triplets that sum to zero. The key challenge is **avoiding duplicates** while keeping the algorithm efficient. A naive triple nested loop would be O(n³) and tricky to deduplicate. Instead, we **sort** the array and use the **two‑pointer technique** for each fixed first element.

### Why Sorting + Two Pointers?

- Sorting helps in two ways: it lets us use the efficient two‑pointer method (like Two Sum II) for the two-sum part, and it allows us to easily skip duplicate values to avoid duplicate triplets.
- For each index `i` (the first number), we set `left = i+1` and `right = n-1`, then move them inward based on whether the sum of `nums[i] + nums[left] + nums[right]` is less than, greater than, or equal to zero.
- Duplicates are avoided by:
  1. Skipping the same `nums[i]` if it's the same as the previous `nums[i-1]` (after the first).
  2. After finding a valid triplet, moving `left` past duplicates of `nums[left]` and `right` past duplicates of `nums[right]`.

### Algorithm Steps

1. Sort the array `nums`.
2. Initialize an empty list `result`.
3. Loop `i` from `0` to `n-3`:
   - If `nums[i] > 0`: break (since all subsequent numbers are ≥ `nums[i]`, sum cannot be zero).
   - If `i > 0` and `nums[i] == nums[i-1]`: continue (skip duplicate first elements).
   - Set `left = i + 1`, `right = n - 1`.
   - While `left < right`:
     - Compute `total = nums[i] + nums[left] + nums[right]`.
     - If `total < 0`: increment `left`.
     - Else if `total > 0`: decrement `right`.
     - Else (`total == 0`):
       - Append `[nums[i], nums[left], nums[right]]` to `result`.
       - Move `left` to the next different number: while `left < right` and `nums[left] == nums[left+1]`: `left += 1`.
       - Move `right` to the previous different number: while `left < right` and `nums[right] == nums[right-1]`: `right -= 1`.
       - Then, finally `left += 1`, `right -= 1` to move past the matched pair.
4. Return `result`.

## Complexity Analysis

- **Time Complexity:** O(n²)  
  Sorting takes O(n log n). The outer loop runs O(n) times, and the inner two‑pointer loop runs in O(n) for each outer iteration. Overall O(n²).
- **Space Complexity:** O(1) (or O(n) for sorting, depending on the sorting algorithm). The output list is not considered extra space. The algorithm uses only a few pointers.

## Code (Python)

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # If the smallest number is positive, sum can't be zero
        if nums[i] > 0:
            break

        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward after storing the triplet
                left += 1
                right -= 1

    return result
```

## Edge Cases

- **Array length < 3:** returns `[]`.
- **All positive or all negative numbers:** no triplet can sum to zero → `[]`.
- **All zeros:** returns `[[0,0,0]]` exactly once.
- **Duplicate zeros and other numbers:** only unique triplets are kept.
- **Large input (up to 3000 elements):** O(n²) is acceptable.

## Alternative Approaches

| Approach                         | Time  | Space | Notes                                                                                                                                                        |
| -------------------------------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Brute force (three nested loops) | O(n³) | O(1)  | Too slow, and deduplication is cumbersome.                                                                                                                   |
| HashSet for complements          | O(n²) | O(n)  | For each `i`, treat as Two Sum on the rest; use set to store pairs; slower than two pointers due to set overhead and requires extra space for deduplication. |
| Sorting + two pointers (above)   | O(n²) | O(1)  | Optimal; no extra space beyond output, and naturally avoids duplicates.                                                                                      |

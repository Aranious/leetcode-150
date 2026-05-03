# 11. Container With Most Water

**Difficulty:** Medium  
**Problem Link:** [LeetCode 11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x‑axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Note:** You may not slant the container.

## Examples

| Input                          | Output | Explanation                                                                                                                            |
| ------------------------------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `height = [1,8,6,2,5,4,8,3,7]` | `49`   | The maximum area is formed between the lines at index 1 (height 8) and index 8 (height 7). Width = 7, height = min(8,7)=7 → area = 49. |
| `height = [1,1]`               | `1`    | Only two lines; width = 1, height = 1 → area = 1.                                                                                      |

## Approach

The area of water that can be contained between two lines at indices `i` and `j` (with `i < j`) is:

`area = (j - i) * min(height[i], height[j])`

We need to maximize this area.

### 1. Brute Force (Intuitive)

- Consider every possible pair of lines using two nested loops.
- Compute the area for each pair and keep track of the maximum.
- Simple to understand but inefficient for large inputs.

### 2. Two Pointers (Optimal)

The problem can be solved in O(n) time using the two‑pointer technique.

**Key insight:** Start with the widest possible container (`left = 0`, `right = n-1`). The width can only shrink as we move the pointers inward. To possibly find a larger area, we must try to increase the **height**, because area = width × height. The limiting factor is the **shorter** of the two lines. Therefore, we always move the pointer that points to the **shorter** line inward, hoping to find a taller line that may compensate for the reduced width.

### Algorithm Steps (Two Pointers)

1. Initialize `left = 0`, `right = len(height) - 1`, `max_area = 0`.
2. While `left < right`:
   - Compute `width = right - left`.
   - Compute `h = min(height[left], height[right])`.
   - Update `max_area = max(max_area, width * h)`.
   - If `height[left] < height[right]`, increment `left` (move the shorter left side inward).
   - Else, decrement `right` (move the shorter or equal right side inward).
3. Return `max_area`.

## Complexity Analysis

| Method       | Time  | Space |
| ------------ | ----- | ----- |
| Brute Force  | O(n²) | O(1)  |
| Two Pointers | O(n)  | O(1)  |

- **Time Complexity:** O(n) for two‑pointer approach – each element is visited at most once.
- **Space Complexity:** O(1) – only a few integer variables are used.

## Code (Python)

### Brute Force (O(n²) – for understanding)

```python
from typing import List

def maxArea(height: List[int]) -> int:
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area
```

### Two Pointers (Optimal O(n))

```python
from typing import List

def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

## Edge Cases

- **Minimum size (n = 2):** Works correctly; returns the only possible area.
- **All heights equal:** The area will shrink as width decreases; algorithm correctly tracks max.
- **Increasing / decreasing heights:** Two‑pointer approach works regardless of the order.
- **Large input (up to 10⁵):** O(n) time and O(1) space handle it effortlessly.

## Alternative Approaches

| Approach             | Time  | Space | Notes                                                                           |
| -------------------- | ----- | ----- | ------------------------------------------------------------------------------- |
| Brute force          | O(n²) | O(1)  | Too slow for large arrays, but simple to verify correctness.                    |
| Two pointers (above) | O(n)  | O(1)  | Optimal; proof relies on “move shorter line” guarantee.                         |
| Dynamic programming  | N/A   | N/A   | Not a typical DP problem; area depends on two indices, not contiguous subarray. |

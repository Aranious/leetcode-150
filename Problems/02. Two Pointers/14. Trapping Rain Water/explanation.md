# 42. Trapping Rain Water

**Difficulty:** Hard  
**Problem Link:** [LeetCode 42 - Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Examples

| Input                                | Output | Explanation                                                                                  |
| ------------------------------------ | ------ | -------------------------------------------------------------------------------------------- |
| `height = [0,1,0,2,1,0,1,3,2,1,2,1]` | `6`    | The elevation map traps 6 units of water. The peaks at indices 1,3,7,10 form the boundaries. |
| `height = [4,2,0,3,2,5]`             | `9`    | Total trapped water = 9 units.                                                               |
| `height = [1,2,3,4]`                 | `0`    | Monotonically increasing; water cannot be trapped.                                           |
| `height = [3,2,1,2,3]`               | `4`    | A valley shape traps water in the middle.                                                    |

## Approach

At each index `i`, the water that can be trapped above that bar is determined by the **shorter** of the tallest bars to its left and right:

`water[i] = min(left_max[i], right_max[i]) - height[i]`

(If this value is negative, no water is trapped there.)

The total water is the sum over all indices. The challenge is to compute this efficiently.

### 1. Brute Force (O(n²))

For each index, scan to the left to find the maximum height, and scan to the right to find the maximum height. Then calculate `water[i]`. This is simple but too slow for large arrays.

### 2. Prefix/Suffix Arrays (O(n) time, O(n) space)

Precompute two arrays:

- `left_max[i]`: the highest bar from `0` to `i`.
- `right_max[i]`: the highest bar from `i` to `n-1`.
  Then a single pass computes the water at each index. This is O(n) time but uses O(n) extra space.

### 3. Two Pointers (Optimal, O(1) space)

We can compute left and right maxima **on the fly** while moving two pointers inward, achieving O(n) time and O(1) space.

**Key Insight:**  
At any step, if `left_max < right_max`, then the amount of water at index `left` is **only limited by `left_max`**, regardless of the actual right walls further away (because there is a right wall at least as tall as `right_max`). Conversely, if `right_max <= left_max`, water at `right` is limited by `right_max`. So we can safely process the pointer that points to the smaller max, update the water, and move the pointer inward.

### Algorithm Steps (Two Pointers)

1. If the array is empty, return 0.
2. Initialize `left = 0`, `right = len(height) - 1`.
3. Initialize `left_max = height[left]`, `right_max = height[right]`.
4. Initialize `water = 0`.
5. While `left < right`:
   - If `left_max < right_max`:
     - Move `left` one step to the right (`left += 1`).
     - Update `left_max = max(left_max, height[left])`.
     - Add `left_max - height[left]` to `water` (this can be zero if `height[left]` is the new max).
   - Else:
     - Move `right` one step to the left (`right -= 1`).
     - Update `right_max = max(right_max, height[right])`.
     - Add `right_max - height[right]` to `water`.
6. Return `water`.

## Complexity Analysis

| Method                 | Time  | Space |
| ---------------------- | ----- | ----- |
| Brute Force            | O(n²) | O(1)  |
| Prefix/Suffix Arrays   | O(n)  | O(n)  |
| Two Pointers (Optimal) | O(n)  | O(1)  |

- **Time Complexity:** O(n) for two pointers – each index processed exactly once.
- **Space Complexity:** O(1) – only a few variables.

## Code (Python)

### Brute Force (O(n²))

```python
from typing import List

def trap_bruteforce(height: List[int]) -> int:
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i+1])   # max from start to i
        right_max = max(height[i:])    # max from i to end
        water = min(left_max, right_max) - height[i]
        if water > 0:
            total += water
    return total
```

### Prefix/Suffix Arrays (O(n) time, O(n) space)

```python
from typing import List

def trap_prefix_suffix(height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - height[i]
    return total
```

### Two Pointers (Optimal, O(1) space)

```python
from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water
```

## Edge Cases

- **Empty array:** `[]` → `0`.
- **Single or two bars:** Cannot trap water (need a valley) → `0`.
- **Monotonically increasing or decreasing:** No water trapped → `0`.
- **Flat terrain:** All heights equal; no water trapped → `0`.
- **Large array (up to 10⁵):** Two-pointer O(n) handles it efficiently.
- **Negative heights:** Input is non‑negative, but zero is fine.

## Alternative Approaches

| Approach             | Time  | Space | Notes                                                                         |
| -------------------- | ----- | ----- | ----------------------------------------------------------------------------- |
| Brute Force          | O(n²) | O(1)  | Not practical for large inputs.                                               |
| Prefix/Suffix Arrays | O(n)  | O(n)  | Straightforward; good intermediate solution.                                  |
| Two Pointers (above) | O(n)  | O(1)  | Optimal; best balance of time and space.                                      |
| Stack (Monotonic)    | O(n)  | O(n)  | Can compute water by tracking decreasing heights; more complex but also O(n). |

The two‑pointer approach is the most space‑efficient while maintaining linear time.

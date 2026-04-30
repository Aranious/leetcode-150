# 238. Product of Array Except Self

**Difficulty:** Medium  
**Problem Link:** [LeetCode 238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
- You must write an algorithm that runs in **O(n)** time and **without using the division operation**.
- **Follow-up:** Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Examples

| Input                  | Output        | Explanation                                                                   |
| ---------------------- | ------------- | ----------------------------------------------------------------------------- |
| `nums = [1,2,3,4]`     | `[24,12,8,6]` | `2*3*4=24`, `1*3*4=12`, `1*2*4=8`, `1*2*3=6`                                  |
| `nums = [-1,1,0,-3,3]` | `[0,0,9,0,0]` | Contains a zero; product of all non-zero elements is 9, placed at index of 0. |

## Approach

We need the product of all elements _except_ the current one, without using division.  
The key idea: For each index `i`, `answer[i]` is the **product of all elements to the left** multiplied by the **product of all elements to the right**.

### Why Left & Right Products?

- If we precompute prefix products (left side) and suffix products (right side), we can combine them in one pass.
- `prefix[i]` = product of `nums[0..i-1]`
- `suffix[i]` = product of `nums[i+1..n-1]`
- Then `answer[i] = prefix[i] * suffix[i]`.

### Optimized: Two-Pass (No Extra Arrays)

We can compute the answer array in two passes without storing separate `prefix` and `suffix` arrays:

1. **First pass (Left to Right):**  
   Maintain a running product `left` (initialized to 1).  
   For each index `i`, store `left` into `ans[i]`, then multiply `left` by `nums[i]`.  
   After this, `ans[i]` holds the product of all elements to the left of `i`.

2. **Second pass (Right to Left):**  
   Maintain a running product `right` (initialized to 1).  
   For each index `i` (starting from end), multiply `ans[i]` by `right`, then multiply `right` by `nums[i]`.  
   After this, `ans[i]` holds the final product except self.

## Complexity Analysis

- **Time Complexity:** O(n)  
  Two linear traversals through the array.
- **Space Complexity:** O(1) extra space (or O(n) if counting the output array).  
  The output array `ans` is required by the problem and is not considered extra space. No other auxiliary arrays are used.

## Code (Python)

### Brute Force (for understanding, not O(n))

```python
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        answer[i] = prod
    return answer
```

### Optimal O(n) Two-Pass Solution

```python
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n

    # Left pass: store product of all elements to the left of i
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]

    # Right pass: multiply by product of all elements to the right of i
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]

    return ans
```

## Edge Cases

- **Single element:** The problem typically guarantees `n >= 2`, but if `n = 1`, the product of all except itself would be an empty product (1).
- **Zero elements:** If there is one zero, all other results become 0 except the index of the zero gets the product of all non-zero elements. If there are two or more zeros, all entries in `answer` will be 0.
- **Negative numbers:** Signs work correctly; the left/right product approach handles them naturally.
- **Large input size (up to 10⁵):** O(n) time and O(1) extra space meet constraints.

## Alternative Approaches

| Approach                   | Time  | Space      | Notes                                                                                                            |
| -------------------------- | ----- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| Brute force (nested loops) | O(n²) | O(1)       | Too slow for large inputs, not acceptable.                                                                       |
| Prefix & Suffix arrays     | O(n)  | O(n)       | Build separate left and right product arrays, then combine.                                                      |
| Two-pass (above)           | O(n)  | O(1) extra | Most optimal; in-place (except output) and no division.                                                          |
| Logarithm / antilog        | O(n)  | O(n)       | Use log to convert product to sum; imprecise for large numbers.                                                  |
| Division                   | O(n)  | O(1)       | **Not allowed** per problem statement; compute total product then divide by each element, fails if zero present. |

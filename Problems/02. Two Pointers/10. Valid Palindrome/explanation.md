# 125. Valid Palindrome

**Difficulty:** Easy  
**Problem Link:** [LeetCode 125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a palindrome, or_ `false` _otherwise_.

## Examples

| Input                                  | Output  | Explanation                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| `s = "A man, a plan, a canal: Panama"` | `true`  | After filtering and lowercasing: `"amanaplanacanalpanama"` — a palindrome.                                               |
| `s = "race a car"`                     | `false` | After filtering: `"raceacar"` — not a palindrome.                                                                        |
| `s = " "`                              | `true`  | After removing non-alphanumeric characters, `s` becomes an empty string `""`, which reads the same forward and backward. |
| `s = "0P"`                             | `false` | `"0p"` ≠ `"p0"` — case insensitive but digits matter.                                                                    |

## Approach

We need to check whether the string, after ignoring non-alphanumeric characters and case differences, is symmetric.

Two common ways:

1. **String Cleaning + Reverse**
   - Filter to alphanumeric characters, lowercase them, then compare with its reverse.
   - Simple to implement, but uses O(n) extra space for the cleaned string and the reversed copy.

2. **Two Pointers (Optimal)**
   - Place one pointer at the start (`left`) and one at the end (`right`).
   - Skip non-alphanumeric characters while moving pointers inward.
   - Compare the lowercase characters at `left` and `right`. If they differ → not a palindrome.
   - Continue until pointers cross; if all pairs match → it is a palindrome.
   - O(1) extra space (only pointers).

### Algorithm Steps (Two Pointers)

1. Initialize `left = 0`, `right = len(s) - 1`.
2. While `left < right`:
   - Increment `left` while `left < right` and `s[left]` is not alphanumeric.
   - Decrement `right` while `left < right` and `s[right]` is not alphanumeric.
   - If `s[left].lower() != s[right].lower()` → return `False`.
   - Move both pointers inward: `left += 1`, `right -= 1`.
3. Return `True` after the loop.

## Complexity Analysis

| Method              | Time | Space |
| ------------------- | ---- | ----- |
| Filtering + Reverse | O(n) | O(n)  |
| Two Pointers        | O(n) | O(1)  |

- **Time Complexity:** O(n) – each character is processed at most twice (once by each pointer, skipping non‑alphanumeric).
- **Space Complexity:** O(1) for two pointers; O(n) for the filtered‑string approach.

## Code (Python)

### Filtered String + Reverse (Simple)

```python
def isPalindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
```

### Two Pointers (Optimal)

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare after lowercasing
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

## Edge Cases

- **Empty string or only non‑alphanumeric:** `" "`, `"."`, `",."` → true, as the filtered string is empty.
- **Single character:** `"a"`, `"Z"`, `"5"` → always true.
- **Numbers only:** `"121"` → true; `"123"` → false. Digits are alphanumeric.
- **Mixed case:** `"Aba"` → true after lowercasing.
- **Large input:** O(n) time with O(1) extra space handles length up to `2*10^5` comfortably.

## Alternative Approaches

| Approach                            | Time | Space | Notes                                                                  |
| ----------------------------------- | ---- | ----- | ---------------------------------------------------------------------- |
| Brute force: filter, reverse        | O(n) | O(n)  | Clean, readable, but not space‑optimal.                                |
| Two pointers (above)                | O(n) | O(1)  | Optimal; no extra memory beyond pointers.                              |
| Recursive (head & tail)             | O(n) | O(n)  | Recursion stack space; not recommended due to possible deep recursion. |
| Using regex to clean `[^a-zA-Z0-9]` | O(n) | O(n)  | Same as filtering, regex can be slower; not necessary.                 |

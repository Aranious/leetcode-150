# 76. Minimum Window Substring

**Difficulty:** Hard  
**Problem Link:** [LeetCode 76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

- The testcases will be generated such that **the answer is unique**.
- A **substring** is a contiguous sequence of characters within the string.

## Examples

| Input                              | Output   | Explanation                                                                                                                            |
| ---------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `s = "ADOBECODEBANC"`, `t = "ABC"` | `"BANC"` | The minimum window that contains A, B, C is `"BANC"`. `"ADOBEC"` and `"CODEBANC"` are longer windows that also contain all characters. |
| `s = "a"`, `t = "a"`               | `"a"`    | The entire string is the minimum window.                                                                                               |
| `s = "a"`, `t = "aa"`              | `""`     | `s` does not have two `'a'`s, so no window can contain all characters of `t`.                                                          |
| `s = "ab"`, `t = "a"`              | `"a"`    | Single character `"a"` is the smallest substring that contains `"a"`.                                                                  |
| `s = "ab"`, `t = "b"`              | `"b"`    | Similar.                                                                                                                               |

## Approach

We need to find the smallest substring of `s` that covers all characters (including duplicates) of `t`. This is a classic **sliding window** problem where we expand a window until it's valid, then contract it from the left while maintaining validity to find the minimum length.

### Why Sliding Window with Character Counting?

- We maintain two hash maps: `need` (the frequency of characters required in `t`) and `window` (the frequency of characters in the current window of `s`).
- We track how many distinct characters have been fully satisfied (i.e., their count in the window meets or exceeds the count in `need`) using an integer `formed`.
- When `formed == required` (the number of unique characters in `need`), the window is valid. We then try to shrink it from the left as much as possible while it remains valid – this gives us the minimum window ending at the current right index.
- Continue sliding the right pointer across `s`. The answer is the smallest valid window encountered.

### Algorithm Steps

1. If `s` or `t` is empty, return `""`.
2. Build `need` dictionary from `t`: map each character to its required frequency.
3. Initialize `left = 0`, `formed = 0`, `required = len(need)`.
4. Initialize `window` (empty dictionary), `min_len = inf`, `min_start = 0`.
5. Iterate `right` from `0` to `len(s)-1`:
   - Add `s[right]` to `window`, increment its count.
   - If `s[right]` is in `need` and its count in `window` now equals `need[s[right]]`, increment `formed`.
   - **While** `formed == required` (the window is valid):
     - Compute current window length `cur_len = right - left + 1`.
     - If `cur_len < min_len`, update `min_len = cur_len` and `min_start = left`.
     - Remove `s[left]` from the window: decrement its count. If it is a key in `need` and its count falls below the required amount, decrement `formed`.
     - Increment `left` (shrink window).
6. After the loop, if `min_len == inf`, return `""`. Otherwise return `s[min_start:min_start+min_len]`.

## Complexity Analysis

- **Time Complexity:** O(|s| + |t|)  
  Both `right` and `left` traverse the string `s` at most once. Hash map operations (insert, update, get) are O(1) on average. Building `need` takes O(|t|).
- **Space Complexity:** O(|s| + |t|) in the worst case for the two dictionaries (but character sets are often bounded, e.g., ASCII 128, so can be considered O(1) extra space). In practice, `window` may hold at most |s| distinct characters, but usually much less.

## Code (Python)

```python
def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # Dictionary for characters required by t
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    left = 0
    formed = 0
    required = len(need)
    window = {}
    min_len = float('inf')
    min_start = 0

    for right, char in enumerate(s):
        # Expand window to the right
        window[char] = window.get(char, 0) + 1

        # If current character's count matches required amount, one more character is satisfied
        if char in need and window[char] == need[char]:
            formed += 1

        # Try to contract window from the left while valid
        while left <= right and formed == required:
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
                min_start = left

            # Remove leftmost character
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float('inf') else ""
```

## Edge Cases

- **Empty strings:** If `s` or `t` is empty → return `""`.
- **t longer than s:** No possible window → return `""`.
- **t contains characters not present in s:** The algorithm naturally handles it because `formed` will never reach `required` → returns `""`.
- **Multiple same characters in t:** Frequency maps ensure that duplicates are correctly accounted for.
- **Minimum window at the very beginning or end of s:** The sliding window correctly finds it because we check all valid windows.
- **Very large strings:** O(n) time still efficient for constraints (e.g., up to 10^5).

## Alternative Approaches

| Approach                                         | Time                            | Space                  | Notes                                                                                            |
| ------------------------------------------------ | ------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------ |
| Brute force (enumerate all substrings)           | O(\|s\|³) or O(\|s\|² \* \|t\|) | O(1) except substrings | Impractical for large inputs.                                                                    |
| Sliding window + hash maps (above)               | O(\|s\| + \|t\|)                | O(character set)       | Optimal; works for any characters.                                                               |
| Sliding window with array of size 128/256        | O(\|s\| + \|t\|)                | O(1)                   | Slightly faster if character set is limited (e.g., ASCII). No dictionary overhead.               |
| Optimized sliding window (skip non‑t characters) | O(\|s\| + \|t\|)                | O(\|t\|)               | Preprocess `s` to only consider indices containing characters from `t`; reduces constant factor. |

The provided hash‑map sliding window solution is clean, easy to understand, and meets all requirements.

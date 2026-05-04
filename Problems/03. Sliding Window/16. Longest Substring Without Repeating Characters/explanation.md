# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

A substring is a contiguous block of characters in the string.

## Examples

| Input            | Output | Explanation                                                                                |
| ---------------- | ------ | ------------------------------------------------------------------------------------------ |
| `s = "abcabcbb"` | `3`    | The answer is `"abc"`, with the length of 3.                                               |
| `s = "bbbbb"`    | `1`    | The answer is `"b"`, with the length of 1.                                                 |
| `s = "pwwkew"`   | `3`    | The answer is `"wke"`, with the length of 3. (`"pwke"` is a subsequence, not a substring). |
| `s = ""`         | `0`    | Empty string → length 0.                                                                   |
| `s = "abcva"`    | `4`    | The longest substring without repeats is `"abcv"` or `"bcva"`.                             |

## Approach

We need to find the maximum length of a substring that contains all unique characters. A naive O(n²) approach would check every possible substring, but we can do better with the **sliding window** technique.

### Why Sliding Window?

- A sliding window maintains two pointers (`left` and `right`) that define the current substring.
- As we expand the window to the right, we add characters. If a character is already in the window, we shrink the window from the left until the duplicate is removed.
- This ensures we never need to restart from each possible start position; instead, we smoothly slide the window across the string in O(n) time.

### Data Structures

- A hash set (or a dictionary for character frequencies) to track characters currently inside the window. For best efficiency, a set works because we only need to know presence/absence.

### Algorithm Steps (Sliding Window + Set)

1. Initialize `seen = set()` (stores characters currently in the window).
2. Initialize `left = 0`, `max_len = 0`.
3. Iterate `right` from `0` to `len(s) - 1`:
   - **While `s[right]` is already in `seen`** (i.e., window has duplicate):
     - Remove `s[left]` from `seen`.
     - Increment `left` by 1 (shrink window from left).
   - Add `s[right]` to `seen`.
   - Update `max_len = max(max_len, right - left + 1)`.
4. Return `max_len`.

### Alternative Sliding Window (using a dictionary to store indices)

We can also use a dictionary to map a character to its most recent index. When a duplicate is found, we can jump `left` directly to `max(left, index[char] + 1)`, which avoids the inner while loop and makes it strictly O(n) without worst-case O(2n) removal steps. Both are O(n) time, but the dictionary version may be slightly more efficient.

## Complexity Analysis

| Method                            | Time  | Space                           | Notes                                                                               |
| --------------------------------- | ----- | ------------------------------- | ----------------------------------------------------------------------------------- |
| Brute force (all substrings)      | O(n²) | O(k) where k character set size | Too slow for large n (n up to 5\*10^4).                                             |
| Sliding Window + Set (above)      | O(n)  | O(min(n, m))                    | m = size of character set (e.g., 128 for ASCII). Each char processed at most twice. |
| Sliding Window + Dict (optimized) | O(n)  | O(min(n, m))                    | Jumps left pointer, potentially fewer operations.                                   |

- **Time Complexity:** O(n) — each character is added to the set once and removed at most once.
- **Space Complexity:** O(min(n, m)) — in the worst case (all distinct characters), we store them all; but the set size is bounded by the size of the character set (e.g., 128 ASCII, 26 lowercase letters, etc.).

## Code (Python)

### Brute Force (O(n²))

```python
def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, len(seen))
            else:
                break
    return longest
```

### Sliding Window with Set (Optimal)

```python
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:      # duplicate found, shrink window
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

### Sliding Window with Dictionary (Jump optimization)

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1   # jump directly past the duplicate
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

## Edge Cases

- **Empty string:** returns `0`.
- **Single character:** returns `1`.
- **All identical:** `"aaaa"` → `1`.
- **String with spaces, digits, symbols:** The approach works for any valid ASCII character; `isalnum()` is not used, we just compare characters directly.
- **Repeating pattern:** `"abcabcbb"` → `3`; window correctly resets after a duplicate.
- **Large input size:** Up to 5×10⁴ characters; O(n) time with O(128) constant space handles it efficiently.

## Alternative Approaches

| Approach                              | Time  | Space        | Notes                                                                                            |
| ------------------------------------- | ----- | ------------ | ------------------------------------------------------------------------------------------------ |
| Brute force (nested loops)            | O(n²) | O(k)         | Too slow; fails for longer strings.                                                              |
| Sliding Window + Set (above)          | O(n)  | O(min(n, m)) | Simple, efficient.                                                                               |
| Sliding Window + Dict (above)         | O(n)  | O(min(n, m)) | Slightly more efficient by skipping left to last occurrence index.                               |
| Integer bitmask (for limited charset) | O(n)  | O(1)         | For only lowercase letters, use a 26-bit integer as a set; extremely fast but charset-dependent. |

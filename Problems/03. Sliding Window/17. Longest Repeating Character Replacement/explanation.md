# 424. Longest Repeating Character Replacement

**Difficulty:** Medium  
**Problem Link:** [LeetCode 424 - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation **at most** `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

| Input                  | Output | Explanation                                                                                                |
| ---------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| `s = "ABAB", k = 2`    | `4`    | Replace two 'A's with 'B's (or vice versa) → entire string becomes "AAAA" or "BBBB".                       |
| `s = "AABABBA", k = 1` | `4`    | Replace the one 'B' in the middle (e.g., "AABABBA" → "AAAABBA") yields longest repeating substring "AAAA". |
| `s = "ABCDE", k = 1`   | `2`    | You can change one character to match its neighbor; max substring length is 2.                             |
| `s = "AAAA", k = 2`    | `4`    | Already all same; no replacements needed.                                                                  |

## Approach

We need to find the longest substring where the **number of characters that are not the most frequent one is ≤ k**.  
If we can change up to `k` characters, we can make the whole window uniform if:

```
window length - max_frequency_of_any_char_in_window ≤ k
```

This is the **sliding window** technique.

### Why Sliding Window?

- Maintain a window `[left, right]`.
- Keep a frequency count of characters in the current window.
- Track `max_freq` (the count of the most frequent character in the window).  
  **Note:** We do not need to recompute `max_freq` from scratch when the window shrinks; it's safe to keep the historical maximum because it only makes the validity check slightly stricter — if a smaller actual max_freq still satisfies the condition, the window is still valid. This lazy update avoids a O(26) scan and keeps O(1) per step.
- When `(window length) - max_freq > k`, the window is invalid → we shrink from the left by moving `left` and decrementing the count of `s[left]`.
- The answer is the maximum window size seen that was valid.

### Algorithm Steps

1. Initialize `count` dictionary (or array of size 26) to store character frequencies.
2. Initialize `left = 0`, `max_freq = 0`, `max_len = 0`.
3. Iterate `right` from `0` to `len(s)-1`:
   - Character `ch = s[right]`. Increment `count[ch]`.
   - Update `max_freq = max(max_freq, count[ch])`.
   - While `(right - left + 1) - max_freq > k`:
     - Decrement `count[s[left]]`.
     - Increment `left`.
   - Update `max_len = max(max_len, right - left + 1)`.
4. Return `max_len`.

## Complexity Analysis

- **Time Complexity:** O(n)  
  Both `left` and `right` move at most n steps. Hash map operations are O(1).
- **Space Complexity:** O(1) (or O(26) for the frequency array)  
  The character set is fixed (uppercase English letters), so the dictionary/array size is bounded by 26.

## Code (Python)

### Brute Force (O(n²)) – for reference

```python
def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        freq = {}
        max_f = 0
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_f = max(max_f, freq[s[j]])
            if (j - i + 1) - max_f <= k:
                ans = max(ans, j - i + 1)
    return ans
```

### Sliding Window (Optimal O(n))

```python
def characterReplacement(s: str, k: int) -> int:
    count = {}  # character -> frequency in current window
    max_freq = 0
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])

        # If window is invalid, shrink it
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Using fixed-size array for 26 letters

```python
def characterReplacement(s: str, k: int) -> int:
    freq = [0] * 26
    max_freq = left = max_len = 0

    for right, ch in enumerate(s):
        idx = ord(ch) - ord('A')
        freq[idx] += 1
        max_freq = max(max_freq, freq[idx])

        if (right - left + 1) - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

## Edge Cases

- **Empty string** → `0`.
- **k = 0** → the longest substring without any replacement, i.e., the longest run of a single character.
- **All characters the same** → answer is `len(s)`, regardless of k.
- **k ≥ len(s)** → the whole string can be converted to one character, answer is `len(s)`.
- **String with multiple long runs and limited k** → window correctly shrinks when needed.

## Alternative Approaches

| Approach                                  | Time   | Space | Notes                                                                                        |
| ----------------------------------------- | ------ | ----- | -------------------------------------------------------------------------------------------- |
| Brute force (all substrings)              | O(n²)  | O(1)  | Too slow for large n (up to 10⁵).                                                            |
| Sliding window + max_freq pruning (above) | O(n)   | O(1)  | Optimal. The lazy update of max_freq works because we only care about window validity.       |
| Sliding window with full frequency scan   | O(26n) | O(1)  | Less efficient but still O(n); after shrinking we recompute max_freq by scanning 26 letters. |

The lazy `max_freq` update is a smart trick: even if the actual maximum frequency in the window drops, we keep the larger `max_freq` because it only makes the condition `window - max_freq > k` _harder_ to satisfy, which never misses a valid window but may shrink a bit more than strictly necessary. This does not affect the final answer because the window size only grows; we just keep moving left forward.

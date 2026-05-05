# 567. Permutation in String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 567 - Permutation in String](https://leetcode.com/problems/permutation-in-string/)

## Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a **permutation** of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

## Examples

| Input                          | Output  | Explanation                                                         |
| ------------------------------ | ------- | ------------------------------------------------------------------- |
| `s1 = "ab"`, `s2 = "eidbaooo"` | `true`  | `s2` contains `"ba"`, which is a permutation of `"ab"`.             |
| `s1 = "ab"`, `s2 = "eidboaoo"` | `false` | No permutation of `"ab"` appears as a contiguous substring in `s2`. |
| `s1 = "adc"`, `s2 = "dcda"`    | `true`  | `"cda"` is a permutation of `"adc"`.                                |
| `s1 = "a"`, `s2 = "ab"`        | `true`  | Single character `"a"` is trivially contained.                      |
| `s1 = "abc"`, `s2 = "def"`     | `false` | No characters match → no permutation possible.                      |

## Approach

We need to check whether any substring of `s2` of length equal to `len(s1)` has the exact same character frequencies as `s1`.

### Why Sliding Window?

- The window size is fixed = `len(s1)`.
- We can slide this window across `s2`, updating frequency counts incrementally, and compare against the target frequency map of `s1`.
- This avoids re‑counting the whole window for every position, reducing time to O(n).

### Algorithm Steps

1. If `len(s1) > len(s2)`, return `False` immediately.
2. Build target frequency map/array for `s1`.
3. Build initial frequency map/array for the first `L` characters of `s2`.
4. If they match, return `True`.
5. Slide the window rightward from index `L` to the end:
   - Add the new character on the right.
   - Remove the character that just left the window on the left (index `i - L`).
   - Clean up zero counts only if using a dictionary (not necessary for fixed‑size arrays).
   - If the window's frequency map equals the target map, return `True`.
6. If the loop finishes without a match, return `False`.

## Complexity Analysis

- **Time Complexity:** O(n) where n = len(s2). We iterate through `s2` once, and comparison of frequency maps is O(1) when using fixed‑size arrays (26 comparisons) or effectively O(1) for dictionaries if character set is small.
- **Space Complexity:** O(1) using two integer arrays of size 26 (or at most O(26) for dictionaries).

## Code (Python)

### Using `Counter` (dictionary)

```python
from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    L = len(s1)
    c1 = Counter(s1)
    c2 = Counter(s2[:L])

    if c1 == c2:
        return True

    for i in range(L, len(s2)):
        c2[s2[i]] += 1
        c2[s2[i - L]] -= 1
        # Remove zero-count entries to keep comparison exact
        if c2[s2[i - L]] == 0:
            del c2[s2[i - L]]
        if c1 == c2:
            return True

    return False
```

### Using Fixed-Size Array (Optimal for lowercase letters only)

```python
def checkInclusion(s1: str, s2: str) -> bool:
    L = len(s1)
    n = len(s2)
    if L > n:
        return False

    target = [0] * 26
    window = [0] * 26

    for c in s1:
        target[ord(c) - ord('a')] += 1

    # Initial window
    for i in range(L):
        window[ord(s2[i]) - ord('a')] += 1
    if window == target:
        return True

    # Slide the window
    for i in range(L, n):
        window[ord(s2[i]) - ord('a')] += 1
        window[ord(s2[i - L]) - ord('a')] -= 1
        if window == target:
            return True

    return False
```

## Edge Cases

- **s1 longer than s2** → immediately return `False`.
- **s1 = s2** → return `True` (entire string is a permutation).
- **Duplicate characters** → both counting methods handle frequency correctly (e.g., `s1="aa"` requires exactly two `'a'`s).
- **Non‑lowercase or extended ASCII** → the array method assumes 26 lowercase letters; for general Unicode, use the Counter approach.
- **Empty s1** → usually `len(s1) <= len(s2)` and an empty window would trivially match (if that's allowed). Problem constraints typically give non‑empty strings.

## Alternative Approaches

| Approach                                | Time       | Space | Notes                                                                           |
| --------------------------------------- | ---------- | ----- | ------------------------------------------------------------------------------- |
| Brute force (generate all permutations) | O(L! \* N) | O(1)  | Completely impractical for even moderate `L`.                                   |
| Sliding window + Counter (above)        | O(n)       | O(1)  | Clean and works for any character set.                                          |
| Sliding window + array (above)          | O(n)       | O(1)  | Slightly faster for lowercase alphabetic strings; array comparison is O(26).    |
| Sliding window + hash of frequencies    | O(n)       | O(1)  | Overkill; hashing the frequency tuples is equivalent to comparing arrays/dicts. |

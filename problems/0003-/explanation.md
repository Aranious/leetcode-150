# 242. Valid Anagram

**Difficulty:** Easy  
**Problem Link:** [LeetCode 242 - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

| Input                            | Output  | Explanation                   |
| -------------------------------- | ------- | ----------------------------- |
| `s = "anagram"`, `t = "nagaram"` | `true`  | Same letters rearranged.      |
| `s = "rat"`, `t = "car"`         | `false` | Different sets of characters. |

## Approach

We use a **Hash Map (Dictionary)** to count character frequencies. This approach works for any valid character, not just lowercase English letters.

### Why a Hash Map?

- Two strings are anagrams if they have the same length and the exact same character frequencies.
- We can iterate through `s`, building a frequency dictionary, then iterate through `t` decrementing the counts.
- If at any point a character in `t` is missing from the dictionary or its count would go below zero, the strings are **not** anagrams.
- This gives us O(n) time with O(k) space, where k is the number of unique characters.

### Algorithm Steps

1. **Length Check:** If `len(s) != len(t)`, return `false` immediately (anagrams must have the same length).
2. **Build frequency map from `s`:**
   - Initialize an empty dictionary `freq`.
   - For each character `ch` in `s`:
     - Increment `freq[ch]` by 1 (using `freq.get(ch, 0) + 1` for safe insertion).
3. **Validate with `t`:**
   - For each character `ch` in `t`:
     - If `ch` is **not** present in `freq` or `freq[ch] == 0`, return `false` (either the character is new or we have seen it too many times).
     - Otherwise, decrement `freq[ch]` by 1.
4. If the loop completes without returning `false`, all characters matched perfectly → return `true`.

## Complexity Analysis

- **Time Complexity:** O(n)  
  We traverse both strings exactly once. Each dictionary operation (get, set, check) is O(1) on average.
- **Space Complexity:** O(k)  
  k is the number of distinct characters in `s`. In the worst case (all unique), up to n entries; for Unicode, k could be large, but for most problems it is bounded by the alphabet size.

## Code (Python)

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True
```

## Edge Cases

- Strings of different lengths → `false` (early length check).
- Empty strings `s = ""`, `t = ""` → both empty → `freq` stays empty, `t` loop doesn't run → `true`.
- Works with any Unicode characters (the dictionary accepts any hashable key).
- Single character strings: `"a"`, `"a"` → `true`; `"a"`, `"b"` → `false`.

## Alternative Approaches

| Approach                             | Time       | Space                        | Notes                                                             |
| ------------------------------------ | ---------- | ---------------------------- | ----------------------------------------------------------------- |
| Sorting and comparing                | O(n log n) | O(n) or O(1) (in‑place sort) | Simple but slower; modifies input or requires extra memory.       |
| Frequency array (only lowercase a‑z) | O(n)       | O(1) (26 integers)           | Faster and constant space, but limited to specific character set. |
| Hash map / Dictionary (above)        | O(n)       | O(k), k ≤ unique characters  | General, works for any character set; early exit possible.        |
| `collections.Counter`                | O(n)       | O(k)                         | One‑liner: `return Counter(s) == Counter(t)`; hides the loop.     |

## elegant one‑liner using Counter

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

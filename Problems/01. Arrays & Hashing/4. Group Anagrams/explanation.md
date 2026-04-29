# 49. Group Anagrams

**Difficulty:** Medium  
**Problem Link:** [LeetCode 49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## Problem Statement

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

| Input                                          | Output                                        | Explanation                                                                        |
| ---------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| `strs = ["eat","tea","tan","ate","nat","bat"]` | `[["bat"],["nat","tan"],["ate","eat","tea"]]` | "ate", "eat", "tea" are anagrams; "nat", "tan" are anagrams; "bat" has no anagram. |
| `strs = [""]`                                  | `[[""]]`                                      | A single empty string groups itself.                                               |
| `strs = ["a"]`                                 | `[["a"]]`                                     | A single character string groups itself.                                           |

## Approach

We use a **hash map** (dictionary) to group strings that share the same "anagram signature".

### Why a Hash Map?

- Anagrams, when sorted or when their character frequencies are counted, produce the same key.
- A dictionary can map each key to a list of strings that belong to that anagram group.
- `defaultdict(list)` simplifies appending without explicit key checks.

### Two Common Key Strategies

1. **Sorted String:**  
   Sort the characters of each word. All anagrams yield the same sorted string.  
   _Time per word:_ O(k log k) where k is the string length.

2. **Character Count Tuple:**  
   Count the frequency of each of the 26 lowercase letters (assuming only 'a'–'z').  
   Use the resulting 26-element tuple as the key.  
   _Time per word:_ O(k).

### Algorithm Steps (Character Count Method)

1. Create a `defaultdict(list)` called `groups`.
2. For each string `s` in `strs`:
   - Initialize a list `count` of 26 zeros (or a fixed-size array).
   - For each character `ch` in `s`, increment the corresponding position: `ord(ch) - ord('a')`.
   - Convert `count` to a tuple (`tuple(count)`) to use as a dictionary key.
   - Append `s` to `groups[key]`.
3. Return the dictionary values as a list of lists.

## Complexity Analysis

- **Time Complexity:** O(n · k) for the count method, where n = number of strings, k = maximum length of a string.  
  O(n · k log k) for the sorting method.
- **Space Complexity:** O(n · k) to store all strings in the output and the hash map keys.

## Code (Python)

### Character Count Version (Optimal)

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())
```

### Sorted String Version (Concise)

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
```

## Edge Cases

- Empty input list → returns empty list `[]`.
- Array containing one empty string → `[[""]]`.
- All strings identical → one big group.
- Strings of varying lengths → only same length strings can be anagrams; different lengths automatically fall into separate groups.
- Very large strings or many strings (up to 10⁴ elements) → both approaches are efficient enough.

## Alternative Approaches

| Approach                       | Time         | Space  | Notes                                                                        |
| ------------------------------ | ------------ | ------ | ---------------------------------------------------------------------------- |
| Sorted String Key              | O(n·k log k) | O(n·k) | Simplest to implement; sorting overhead may be noticeable for long strings.  |
| Character Count Tuple (above)  | O(n·k)       | O(n·k) | Fastest for large strings; assumes fixed 26 letters.                         |
| Prime‑Product Key (not common) | O(n·k)       | O(n·k) | Maps each letter to a unique prime, key = product; risk of integer overflow. |

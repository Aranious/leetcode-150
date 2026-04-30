# 271. Encode and Decode Strings

**Difficulty:** Medium  
**Problem Link:** [LeetCode 271 - Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

## Problem Statement

Design an algorithm to **encode** a list of strings into a single string, and **decode** that single string back into the original list of strings.

- You must implement two functions:
  - `encode(strs: List[str]) -> str` – Converts a list of strings into a single encoded string.
  - `decode(s: str) -> List[str]` – Converts the encoded string back into the original list of strings.
- The encoded string is sent over the network from Machine 1 to Machine 2, where it is decoded.
- You are **not allowed** to use built-in serialization methods (e.g., `eval`).
- The strings in the list can contain **any valid ASCII characters**, including special characters, spaces, and digits.

## Examples

| Input (strs)             | Encoded (example)      | Decoded (strs)           | Explanation                                                                   |
| ------------------------ | ---------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `["Hello","World"]`      | `"5#Hello5#World"`     | `["Hello","World"]`      | "Hello" has length 5, "World" has length 5.                                   |
| `[""]`                   | `"0#"`                 | `[""]`                   | A single empty string: length = 0, followed by delimiter, then empty string.  |
| `[]`                     | `""`                   | `[]`                     | Empty list encodes to empty string; decode returns empty list.                |
| `["we","say",":","yes"]` | `"2#we3#say1#:3#yes"`  | `["we","say",":","yes"]` | Strings contain special characters (`:`) and have varying lengths.            |
| `["longerString","a"]`   | `"12#longerString1#a"` | `["longerString","a"]`   | Mixed lengths. Length digits ≠ string content even if strings contain digits. |

## Approach

We cannot use a simple delimiter (e.g., `,` or `|`) because the original strings could contain the same character, making it impossible to determine boundaries during decoding. Instead, we **prefix each string with its length and a special separator character**.

### Why Length-Prefix Encoding?

- Each string is stored as `length + delimiter + string`.
- The delimiter (`#`) marks the end of the length digits.
- The length tells us exactly how many characters to read next, regardless of whether those characters include `#`, digits, or spaces.
- This eliminates ambiguity completely and works for any string content.

### Key Insight

During decoding, we:

1. Read characters until we find `#` (these characters represent the integer length of the next string).
2. Skip the `#`.
3. Read exactly that many characters as the next original string.
4. Repeat until the encoded string is fully consumed.

### Algorithm Steps (Encode)

1. If the input list is empty, return an empty string.
2. Initialize an empty result string `encoded`.
3. For each `s` in the input list `strs`:
   - Concatenate `str(len(s)) + "#" + s` to `encoded`.
4. Return `encoded`.

### Algorithm Steps (Decode)

1. If the input string is empty, return an empty list.
2. Initialize `decoded = []` and a pointer `i = 0`.
3. While `i < len(s)`:
   - Move a pointer `j` from `i` until `s[j]` equals `'#'`.
   - Convert the substring `s[i:j]` to an integer representing the length.
   - Set the start of the string to `j + 1`.
   - Read exactly `length` characters starting from `j + 1`.
   - Append this substring to `decoded`.
   - Advance `i` to `j + 1 + length`.
4. Return `decoded`.

## Complexity Analysis

- **Time Complexity:** O(m) for both `encode()` and `decode()`, where `m` is the total sum of the lengths of all strings in the original list.  
  Each character is read exactly once during encoding, and exactly once during decoding.
- **Space Complexity:** O(m + n) where `n` is the number of strings, to store the encoded string (which includes length digits and delimiters) and the final decoded list.
  - Encoding uses O(m + n) to build the result string.
  - Decoding uses O(m + n) for the output list and temporary variables.

## Code (Python)

### Optimal: Length-Prefix with Delimiter `#`

```python
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            # Store length, a delimiter, and the string itself
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            j = i
            # Find the delimiter to extract the length
            while s[j] != '#':
                j += 1
            length = int(s[i:j])        # Length of the next string
            i = j + 1                   # Skip the '#'
            j = i + length              # End of the actual string
            decoded.append(s[i:j])      # Extract the string
            i = j                       # Move to the next encoded segment
        return decoded
```

### Alternative: Chunked Length & Sizes (NeetCode)

```python
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz) + ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1  # skip '#'
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res
```

## Edge Cases

- **Empty list:** `encode([])` should return `""`; `decode("")` should return `[]`.
- **Single empty string:** `encode([""])` should return `"0#"` (or `"0000"` in fixed‑width). `decode("0#")` should return `[""]`.
- **Strings that contain the delimiter:** With length‑prefix encoding, the delimiter is only used as a separator _after_ the length, so even if a string contains `#`, it is safely extracted because the decoder knows exactly how many characters to read.
- **Strings that contain digits:** Digits are treated as regular characters; they appear only _after_ the length prefix, so they are never confused with length metadata.
- **Long strings:** The variable‑length `"len#"` scheme supports theoretically any string length (limited by Python's integer conversion). The fixed‑width scheme with 4 digits supports strings up to length 9999.
- **Very large arrays:** Up to 200 strings (per constraints); both encoding and decoding run in linear time relative to total characters.

## Alternative Approaches

| Approach                       | Time | Space    | Notes                                                                                   |
| ------------------------------ | ---- | -------- | --------------------------------------------------------------------------------------- |
| Length–Delimiter `#` (above)   | O(m) | O(m + n) | Simple, robust, works for all ASCII, handles empty strings.                             |
| Fixed‑Width Length (4 digits)  | O(m) | O(m + n) | Avoids delimiter entirely; always reads exactly 4 digits; slightly less human‑readable. |
| Chunked Sizes + `#` (NeetCode) | O(m) | O(m + n) | Separates all length metadata before string data; slightly more complex but equivalent. |
| Simple Delimiter (e.g., `,`)   | O(m) | O(m)     | **Fails** if strings contain the delimiter; not safe for arbitrary input.               |
| Escape‑Character Based         | O(m) | O(m)     | Doubles occurrences of delimiter; error‑prone and complex.                              |
| JSON/Serialization             | O(m) | O(m)     | Not allowed by problem statement (no `eval` or serialize methods).                      |

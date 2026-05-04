# Brute Force (O(n²))
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


# Sliding Window with Set (Optimal)
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


# Sliding Window with Dictionary (Jump optimization)
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
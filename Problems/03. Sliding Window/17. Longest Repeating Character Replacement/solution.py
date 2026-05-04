# Brute Force (O(n²))
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


# Sliding Window (Optimal O(n))
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


# Using fixed-size array for 26 letters
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
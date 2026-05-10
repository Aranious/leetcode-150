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
# Using Counter (dictionary)
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


# Using Fixed-Size Array (Optimal)
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
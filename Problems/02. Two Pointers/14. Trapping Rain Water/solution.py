# Brute Force
from typing import List

def trap_bruteforce(height: List[int]) -> int:
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i+1])   # max from start to i
        right_max = max(height[i:])    # max from i to end
        water = min(left_max, right_max) - height[i]
        if water > 0:
            total += water
    return total


# Prefix/Suffix Arrays
from typing import List

def trap_prefix_suffix(height: List[int]) -> int:
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    total = 0
    for i in range(n):
        total += min(left_max[i], right_max[i]) - height[i]
    return total


# Two Pointers(optimal)
from typing import List

def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water
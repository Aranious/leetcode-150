# Brute Force
from typing import List

def maxArea(height: List[int]) -> int:
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area


# Two Pointers(optimal)
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
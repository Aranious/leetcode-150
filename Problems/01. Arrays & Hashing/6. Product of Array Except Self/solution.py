# Brute Force
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        answer[i] = prod
    return answer



#  Optimal O(n) Two-Pass Solution

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n

    # Left pass: store product of all elements to the left of i
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]

    # Right pass: multiply by product of all elements to the right of i
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]

    return ans
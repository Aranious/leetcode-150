from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    # According to the problem, exactly one solution always exists,
    # so the function will always return inside the loop.
    return []
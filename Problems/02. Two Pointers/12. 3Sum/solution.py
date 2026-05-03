from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # If the smallest number is positive, sum can't be zero
        if nums[i] > 0:
            break

        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward after storing the triplet
                left += 1
                right -= 1

    return result
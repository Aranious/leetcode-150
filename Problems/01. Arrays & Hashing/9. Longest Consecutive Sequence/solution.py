def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:   # start of a sequence
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)

    return longest


# Sorting 
nums = [0,3,7,2,5,8,4,6,0,1]
nums.sort()
longest = 1
current = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        current += 1
    elif nums[i] != nums[i-1]:   # reset if not consecutive and not duplicate
        current = 1
    longest = max(longest, current)
    
print(longest)
        

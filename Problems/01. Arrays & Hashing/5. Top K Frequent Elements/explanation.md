# 347. Top K Frequent Elements

**Difficulty:** Medium  
**Problem Link:** [LeetCode 347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

It is guaranteed that the answer is unique. In other words, the set of the top `k` frequent elements is unique.

## Examples

| Input                           | Output  | Explanation                                                       |
| ------------------------------- | ------- | ----------------------------------------------------------------- |
| `nums = [1,1,1,2,2,3]`, `k = 2` | `[1,2]` | `1` appears three times, `2` appears twice, so top 2 are `[1,2]`. |
| `nums = [1]`, `k = 1`           | `[1]`   | The only element is the most frequent.                            |
| `nums = [1,2]`, `k = 2`         | `[1,2]` | Both appear once, so order does not matter.                       |

## Approach

We need to count frequencies and then extract the top `k`. There are several efficient ways to do this, all using a **hash map** to count occurrences first.

### 1. Sorting (simple)

- Count frequencies using a dictionary or `Counter`.
- Sort the unique elements by their frequency in descending order and take the first `k`.

### 2. Heap (min‑heap of size `k`)

- Count frequencies.
- Use a min‑heap that always stores the `k` most frequent elements seen so far.
- For each element, push `(frequency, element)` to the heap. If the heap size exceeds `k`, pop the smallest frequency.
- After traversing all elements, the heap contains the top `k` frequent elements.

### 3. Bucket Sort (optimal)

- Count frequencies.
- Create an array of buckets where index `i` stores a list of elements that appear exactly `i` times. Maximum frequency ≤ `n`.
- Iterate over the buckets from high to low, collecting elements until we have `k` elements.

### Algorithm Steps (Bucket Sort)

1. Compute frequency of each number using a dictionary `freq`.
2. Create a list `buckets` of length `n+1` (index 0 unused), each initialized as an empty list.
3. Fill the buckets: for each number and its count, append the number to `buckets[count]`.
4. Iterate `i` from `n` down to `1`:
   - For each number in `buckets[i]`, append to result.
   - When the result length reaches `k`, stop and return.

## Complexity Analysis

| Method      | Time       | Space | Notes                                      |
| ----------- | ---------- | ----- | ------------------------------------------ |
| Sorting     | O(n log n) | O(n)  | Bottleneck is sorting the unique elements. |
| Heap        | O(n log k) | O(n)  | Better when `k` is much smaller than `n`.  |
| Bucket Sort | O(n)       | O(n)  | Linear time, optimal for large inputs.     |

- `n` = number of elements in `nums`.

## Code (Python)

### 1. Using Counter and `most_common` (sorting)

```python
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]
```

### 2. Manual frequency + sorting

```python
from collections import defaultdict
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    # Sort keys by frequency descending, take top k
    return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]
```

### 3. Min‑heap (optimal for `k` small)

```python
import heapq
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    min_heap = []
    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for count, num in min_heap]
```

### 4. Bucket Sort (optimal overall)

```python
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for i in range(n, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result  # Should never be reached
```

## Edge Cases

- `k` equals the number of distinct elements → all elements are returned.
- All elements are the same → only one distinct element, so `k = 1` returns that single element.
- Multiple elements with the same frequency → any valid set of size `k` is accepted (order does not matter).
- Very large array (up to 10⁵) → linear time solutions (bucket sort) handle it efficiently.
- Negative numbers or zero → frequency counting works regardless of value.

## Alternative Approaches

| Approach            | Time       | Space | Notes                                                               |
| ------------------- | ---------- | ----- | ------------------------------------------------------------------- |
| Sorting (above)     | O(n log n) | O(n)  | Simple, but slower for large `n`.                                   |
| Min‑heap (above)    | O(n log k) | O(n)  | Good when `k << n`.                                                 |
| Bucket Sort (above) | O(n)       | O(n)  | Linear time, but uses extra bucket array. Best for large inputs.    |
| Quickselect (Hoare) | O(n) avg   | O(n)  | Partition based on frequency; less stable, but average linear time. |

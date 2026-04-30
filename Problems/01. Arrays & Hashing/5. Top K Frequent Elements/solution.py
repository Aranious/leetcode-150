# 1. Using Counter and `most_common` (sorting)

from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]


# 2. Manual frequency + sorting

from collections import defaultdict
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    # Sort keys by frequency descending, take top k
    return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]


# 3. Min‑heap (optimal for `k` small)

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


# 4. Bucket Sort (optimal overall)

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
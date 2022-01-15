from collections import Counter
from heapq import heappush, heappop
from typing import *

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        topK = []
        for num in nums:
            heappush(topK, num)
            if len(topK) > k:
                heappop(topK)
        freq = Counter(topK)
        result = []
        for num in nums:
            if freq[num] > 0:
                freq[num] -= 1
                result.append(num)
        return result
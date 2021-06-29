from typing import List
from functools import lru_cache

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(start1, start2, starting):
            if start1 == len(nums1) or start2 == len(nums2):
                return 0
            if starting == False:
                if nums1[start1] != nums2[start2]:
                    return 0
                else:
                    return 1 + helper(start1 + 1, start2 + 1, False)
            else:
                res1 = res2 = res3 = 0
                if nums1[start1] == nums2[start2]:
                    res1 = 1 + helper(start1 + 1, start2 + 1, False)
                res2 = helper(start1 + 1, start2, True)
                res3 = helper(start1, start2 + 1, True)
                return max(res1, res2, res3)
        return helper(0, 0, True)
                    
            
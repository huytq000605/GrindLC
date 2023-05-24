class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        nums = [(-nums2[i], nums1[i]) for i in range(n)]
        nums.sort()
        pq = []
        s = 0
        result = 0
        for mul, num in nums:
            heappush(pq, num)
            s += num
            if len(pq) > k:
                s -= heappop(pq)
            if len(pq) == k:
                result = max(result, -mul * s)
        return result

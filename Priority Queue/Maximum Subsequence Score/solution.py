class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        nums = sorted([(nums2[i], nums1[i]) for i in range(n)], reverse = True)
        result = 0
        s = 0
        pq = []
        for i in range(n):
            mn, num = nums[i]
            heappush(pq, num)
            s += num
            if len(pq) > k:
                s -= heappop(pq)
            if len(pq) == k:
                result = max(result, s * mn)
        return result

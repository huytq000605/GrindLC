class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        n, m = len(nums1), len(nums2)
        for i in range(n):
            heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while k > 0 and heap:
            _, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j < m-1:
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return result

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        nums1.sort()
        result = math.inf
        for i1 in range(3):
            x = nums2[0] - nums1[i1]
            j = 0
            skip = 0
            for i in range(len(nums1)):
                if j >= len(nums2): break
                if nums2[j] - nums1[i] != x:
                    skip += 1
                    continue
                j += 1
            if skip <= 2:
                result = min(result, x)
        return result
                
            

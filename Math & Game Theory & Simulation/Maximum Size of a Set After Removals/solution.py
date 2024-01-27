class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n =  len(nums1)
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        
        result = set()
        
        # try to take up to n//2 num from nums1 that is not in nums2
        take = 0
        for num in nums1:
            if num not in nums2:
                result.add(num)
                take += 1
            if take == n//2:
                break
        # if we cannot take n//2 num for nums1 that is not in nums2
        # then we can start taking the num that in num2, up to n//2
        if take < n//2:
            for num in nums1:
                if num not in result:
                    result.add(num)
                    take += 1
                if take == n//2:
                    break
        
        # just take up to n//2 num that is not in result
        take = 0
        for num in nums2:
            if num not in result:
                result.add(num)
                take += 1
            if take == n//2:
                break

        return len(result)

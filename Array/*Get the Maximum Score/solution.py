class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:       
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        cur1 = 0
        cur2 = 0
        while i < n and j < m:
            num1, num2 = nums1[i], nums2[j]
            if num1 < num2:
                cur1 += num1
                i += 1
            elif num1 > num2:
                cur2 += num2
                j += 1
            else:
                cur1 = max(cur1, cur2) + num1
                cur2 = cur1
                i += 1
                j += 1
        
        while j < m:
            cur2 += nums2[j]
            j += 1
        while i < n:
            cur1 += nums1[i]
            i += 1
        return max(cur1, cur2) % (10**9 + 7)
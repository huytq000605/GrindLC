class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
        # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
        # arr[i] - arr[j] <= diff
        n = len(nums1)
        nums = [nums1[i] - nums2[i] for i in range(n)]
        result = 0
        def merge_sort(start, end):
            nonlocal result, nums, diff
            if start == end:
                return [nums[start]]
            mid = start + (end - start) // 2
            a1 = merge_sort(start, mid)
            a2 = merge_sort(mid + 1, end)
            j = 0
            for num in a1:
                while j < len(a2) and num - a2[j] > diff:
                    j += 1
                result += len(a2) - j
            a = []
            i, j = 0, 0
            while i < len(a1) or j < len(a2):
                if i == len(a1):
                    a.append(a2[j])
                    j += 1
                elif j == len(a2):
                    a.append(a1[i])
                    i += 1
                else:
                    if a1[i] <= a2[j]:
                        a.append(a1[i])
                        i += 1
                    else:
                        a.append(a2[j])
                        j += 1
            return a
        merge_sort(0, n-1)
        return result
        

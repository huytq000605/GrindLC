class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # F(0, n-1) = F(0, m) + F(m + 1, n-1) + C
        # C = number of reverse pair where i in [0, m] and j in [n+1][n-1]
        # Explanation in General
        result = 0
        
        def merge_sort(start, end):
            nonlocal result
            if start == end:
                return [nums[start]]
            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > right[j] * 2:
                    result += len(left) - i
                    j += 1
                        
                else:
                    i += 1
       
            i, j = 0, 0
            merge_arr = []
            while i < len(left) or j < len(right):
                if i >= len(left):
                    merge_arr.append(right[j])
                    j += 1
                    continue
                if j>= len(right):
                    merge_arr.append(left[i])
                    i += 1
                    continue
                if left[i] <= right[j]:
                    merge_arr.append(left[i])
                    i += 1
                else:
                    merge_arr.append(right[j])
                    j += 1
            return merge_arr
        
        merge_sort(0, len(nums) - 1)
        return result

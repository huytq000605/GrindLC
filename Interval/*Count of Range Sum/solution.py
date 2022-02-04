class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        result = 0
        def merge_sort(start, end):
            nonlocal lower, upper, result
            if start == end:
                return [prefix[start]]
            mid = start + (end-start)//2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            
            i, j = 0, 0
            for left_prefix in left:
                while i < len(right) and right[i] - left_prefix < lower:
                    i += 1
                while j < len(right) and right[j] - left_prefix <= upper:
                    j += 1
                result += j - i
                
            i, j = 0, 0
            arr = []
            while i < len(left) or j < len(right):
                if i >= len(left):
                    arr.append(right[j])
                    j += 1
                    continue
                
                if j >= len(right):
                    arr.append(left[i])
                    i += 1
                    continue
                
                if left[i] <= right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
                    
            return arr
        merge_sort(0, n)
        return result
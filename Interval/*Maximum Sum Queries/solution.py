class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        nums = sorted([(nums1[i], nums2[i]) for i in range(n)])
        queries = sorted([(x, y, i) for i, (x,y) in enumerate(queries)])
        result = [-1 for _ in range(len(queries))]
        
        valid = []
        def binary_search(num):
            start = 0
            end = len(valid)
            while start < end:
                mid = start + (end - start) // 2
                if valid[mid][0] < num:
                    start = mid + 1
                else:
                    end = mid
            return start

        i = n-1
        max_num2 = 0
        for x, y, j in queries[::-1]:
            while i >= 0 and nums[i][0] >= x:
                num2, s = nums[i][1], sum(nums[i])
                # Because we sorted nums by num1, so num1 will always decreasing
                # Then to find a bigger sum, we must got a bigger num2
                # So we only processed when num2 > max_num2
                # But even when num2 > max_num2, there's still situation new_sum < old_sum
                # We will delete old_sum if old_sum <= new_sum
                if num2 > max_num2:
                    max_num2 = num2
                    while valid and valid[-1][1] <= s:
                        valid.pop()
                    valid.append((num2, s))
                i -= 1
            
            if valid:
                idx = binary_search(y)
                if idx < len(valid):
                    result[j] = valid[idx][1]
            
        return result

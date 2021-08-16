class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        biggest = max(nums)
        prefix = [0] * len(nums)
        for i in range(len(prefix)):
            prefix[i] = [0] * biggest
        
        for i in range(len(nums)):
            if i == 0:
                prefix[0][nums[i] - 1] += 1
            else:
                for j in range(biggest):
                    prefix[i][j] = prefix[i-1][j]
                prefix[i][nums[i] - 1] += 1
        
        def cal(arr):
            prev = -1
            result = math.inf
            for i in range(len(arr)):
                if arr[i] > 0:
                    if prev != -1:
                        result = min(result, i - prev)
                    prev = i
            if result == math.inf:
                return -1
            return result
        
                    
        arr = [0] * biggest
        result = [0] * len(queries)
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]
            if left == 0:
                result[i] = cal(prefix[right])
            else:
                for j in range(biggest):
                    arr[j] = prefix[right][j] - prefix[left - 1][j]
                result[i] = cal(arr)
        return result
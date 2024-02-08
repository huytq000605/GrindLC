class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefix = [0 for _ in range(n)]
        for i, num in enumerate(nums):
            if i > 0: prefix[i] = prefix[i-1]
            prefix[i] += num
            
        result = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            mid = bisect.bisect_right(nums, query-1)
            if mid == 0:
                result[i] = prefix[-1] - query * n
                continue
            result[i] += query * mid - prefix[mid - 1]
            result[i] += (prefix[-1] - prefix[mid - 1]) - (n-mid) * query
        return result

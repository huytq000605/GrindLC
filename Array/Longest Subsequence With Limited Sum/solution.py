class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        queries = sorted([(query, idx) for idx, query in enumerate(queries)])
        result = [0 for i in range(len(queries))]
        i = 0
        s = 0
        for query, idx in queries:
            while i < len(nums) and s + nums[i] <= query:
                s += nums[i]
                i += 1
            result[idx] = i
        return result

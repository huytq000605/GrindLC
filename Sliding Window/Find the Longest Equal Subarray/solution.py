class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        result = 0
        d = defaultdict(deque)
        for i, num in enumerate(nums):
            d[num].append(i)
            if len(d[num]) > 1 and (d[num][-1] - d[num][0] - 1 - (len(d[num]) - 2) ) > k:
                d[num].popleft()
            result = max(result, len(d[num]))
        return result

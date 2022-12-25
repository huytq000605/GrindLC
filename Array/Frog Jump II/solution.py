class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # All stones should be used
        # There are 2 ways to go from start to end with no duplicated stones
        n = len(stones)
        result = stones[1] - stones[0]
        for i in range(2, n):
            result = max(result, stones[i] - stones[i-2])
        return result

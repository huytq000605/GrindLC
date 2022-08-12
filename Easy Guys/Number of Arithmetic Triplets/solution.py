class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = defaultdict(int)
        result = 0
        for num in nums:
            if num - diff in seen:
                seen[num] = seen[num-diff] + 1
            else:
                seen[num] = 1
            if seen[num] >= 3:
                result += 1
        return result

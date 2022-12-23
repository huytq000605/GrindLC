class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        seen = defaultdict(int)
        result = 0
        for num in nums:
            sqrt = math.sqrt(num)
            seen[num] = seen[sqrt] + 1
            result = max(result, seen[num])
        if result == 1:
            return -1
        return result
                

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        seen = defaultdict(int)
        for num in nums:
            seen[num % space] += 1
        freq = max(seen.values())
        for num in nums:
            if seen[num % space] == freq:
                return num

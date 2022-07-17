class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        pairs = 0
        for val in counter.values():
            pairs += (val - val % 2)//2
        return [pairs, n - pairs*2]

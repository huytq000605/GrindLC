class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        freq = [0 for _ in range(101)]
        for num in nums: freq[num] += 1
        if not freq[target]: return []
        prev = 0
        for num in range(target):
            prev += freq[num]
        return [prev + i for i in range(freq[target])]
        

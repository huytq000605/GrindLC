class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[n+i//2] if i % 2 == 1 else nums[i//2] for i in range(2*n)]

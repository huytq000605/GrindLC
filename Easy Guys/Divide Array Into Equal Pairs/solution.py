class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for num in freq.keys():
            if freq[num] % 2 == 1:
                return False
        return True
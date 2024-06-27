class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        for num, freq in counter.items():
            if freq == 2:
                result ^= num
        return result

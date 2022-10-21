class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set(nums)
        for num in nums:
            rev = int(str(num)[::-1])
            result.add(rev)
        return len(result)

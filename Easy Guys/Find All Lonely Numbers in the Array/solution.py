class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = Counter(nums)
        result = []
        for num in nums:
            if num + 1 not in seen and num - 1 not in seen and seen[num] == 1:
                result.append(num)
        return result
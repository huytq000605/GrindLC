class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        missing = lower
        for num in nums:
            if missing == num:
                missing += 1
            else:
                result.append([missing, num - 1])
                missing = num+1
        if missing <= upper:
            result.append([missing, upper])
        return result

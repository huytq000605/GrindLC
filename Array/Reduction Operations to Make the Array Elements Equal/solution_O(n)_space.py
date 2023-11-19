class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        cur = 0
        result = 0
        for k in sorted(counter.keys(), reverse = True):
            result += cur
            cur += counter[k]
        return result

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 1
        for num in counter.keys():
            if num == 1:
                result = max(result, counter[num] - (counter[num] % 2 == 0))
                continue
            cur = 0
            while counter[num] >= 2 and num*num in counter:
                num = num*num
                cur += 2
            cur += 1
            result = max(result, cur)
        return result

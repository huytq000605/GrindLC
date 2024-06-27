class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        vs = counter.keys()
        mn = min(vs)
        mx = max(vs)
        for num in range(mn, mx):
            result += max(0, counter[num] - 1)
            counter[num+1] += max(0, counter[num] - 1)
        result += counter[mx] * (counter[mx] - 1) // 2
        return result

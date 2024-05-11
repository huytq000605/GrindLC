class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def at_most(k): # return number of subarrays have at most k elements
            d = defaultdict(int)
            start = 0
            result = 0
            for i in range(len(nums)):
                d[nums[i]] += 1
                while len(d) > k:
                    d[nums[start]] -= 1
                    if d[nums[start]] == 0:
                        d.pop(nums[start])
                    start += 1
                result += (i - start + 1)
            return result
        # total subarrays
        total = len(nums) * (len(nums) + 1) // 2
        start = 1
        end = len(set(nums))
        while start < end:
            mid = start + (end - start) // 2
            if at_most(mid) * 2 >= total:
                end = mid
            else:
                start = mid + 1
        return start

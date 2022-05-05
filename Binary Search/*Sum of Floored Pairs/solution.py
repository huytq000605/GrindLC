class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        result = 0
        while i < n:
            freq = 0
            num = nums[i]
            while i < n and nums[i] == num:
                i += 1
                freq += 1
            j = i
            result += freq * freq
            while j < n:
                div = nums[j] // num
                start, end = j, n-1
                while start < end:
                    mid = start + math.ceil((end - start + 1) / 2)
                    if nums[mid] // num > div:
                        end = mid - 1
                    else:
                        start = mid
                result += freq * div * (start - j + 1)
                result %= 10**9 + 7
                j = start + 1
        return result
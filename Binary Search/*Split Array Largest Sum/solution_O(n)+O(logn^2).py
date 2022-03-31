class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix = [0 for i in range(len(nums))]
        for i, num in enumerate(nums):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] += num
        left_bound_sum = 0
        right_bound_sum = 10**9
        while left_bound_sum < right_bound_sum:
            largest_sum = left_bound_sum + (right_bound_sum - left_bound_sum) // 2
            prev = 0
            k = m
            i = 0
            while i < len(nums) and k > 0:
                start = i
                end = len(nums) - 1
                while start < end:
                    mid = start + math.ceil((end - start + 1) / 2)
                    if prefix[mid] - prev > largest_sum:
                        end = mid - 1
                    else:
                        start = mid
                if prefix[start] - prev > largest_sum:
                    break
                prev = prefix[start]
                i = start + 1
                k -= 1
            if i < len(nums) or k < 0:
                left_bound_sum = largest_sum + 1
            else:
                right_bound_sum = largest_sum
        return left_bound_sum
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(nums):
            current = []
            result = [0 for i in range(len(nums))]
            for idx, num in enumerate(nums):
                if len(current) == 0 or current[-1] < num:
                    current.append(num)
                else:
                    start = 0
                    end = len(current) - 1
                    while start < end:
                        mid = start + (end - start) // 2
                        if current[mid] < num:
                            start = mid + 1
                        else:
                            end = mid
                    current[start] = num
                result[idx] = len(current)
            return result
        
        leftLIS = LIS(nums)
        rightLIS = LIS(nums[::-1])[::-1]
        
        longestMountain = 0
        for i in range(len(nums)):
            if leftLIS[i] > 1 and rightLIS[i] > 1:
                longestMountain = max(longestMountain, leftLIS[i] + rightLIS[i] - 1)
            
        return len(nums) - longestMountain
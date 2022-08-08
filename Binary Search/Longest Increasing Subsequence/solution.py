class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []

        def binary_search(arr, num):
            start, end = 0, len(arr) - 1
            while start < end:
                mid = start + (end - start) // 2
                if arr[mid] >= num:
                    end = mid
                else:
                    start = mid + 1
            return start

        for num in nums:
            if not LIS or LIS[-1] < num:
                LIS.append(num)
            else:
                idx = binary_search(LIS, num)
                LIS[idx] = num
        return len(LIS)

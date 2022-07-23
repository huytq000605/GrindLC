class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0
        n = len(nums)
        prefix = [0 for i in range(n)]
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] += nums[i]

        def merge_sort(start, end):
            nonlocal result, prefix, lower, upper
            if start > end:
                return []
            elif start == end:
                if lower <= prefix[start] <= upper:
                    result += 1
                return [prefix[start]]
            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid+1, end)

            i, j = 0, 0
            for left_prefix in left:
                while i < len(right) and right[i] - left_prefix < lower:
                    i += 1
                while j < len(right) and right[j] - left_prefix <= upper:
                    j += 1
                result += j - i

            i, j = 0, 0
            arr = []
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    arr.append(right[j])
                    j += 1
                else:
                    arr.append(left[i])
                    i += 1

            while i < len(left):
                arr.append(left[i])
                i += 1

            while j < len(right):
                arr.append(right[j])
                j += 1
            return arr
        merge_sort(0, n-1)
        return result

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        nums = [(nums[i], i) for i in range(n)]
        def merge_sort(start, end):
            if start == end:
                return [nums[start]]
            mid = start + (end - start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            i, j = 0, 0
            arr = []
            number_of_right_smaller = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    number_of_right_smaller += 1
                    arr.append(right[j])
                    j += 1
                else:
                    result[left[i][1]] += number_of_right_smaller
                    arr.append(left[i])
                    i += 1

            while i < len(left):
                result[left[i][1]] += number_of_right_smaller
                arr.append(left[i])
                i += 1

            while j < len(right):
                arr.append(right[j])
                j += 1
            return arr
        result = [0 for i in range(n)]
        merge_sort(0, n-1)
        return result

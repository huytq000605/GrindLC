class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Same with Reverse Pairs
				# Array divide and conquer
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        result = [0 for i in range(n)]
        def merge_sort(start, end):
            nonlocal result
            if start == end:
                return [nums[start]]
            mid = start + (end-start) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    result[left[i][1]] += len(right) - j
                    i += 1
                else:
                    j += 1
            
            i, j = 0, 0
            arr = []
            while i < len(left) or j < len(right):
                if i >= len(left):
                    arr.append(right[j])
                    j += 1
                    continue
                    
                if j >= len(right):
                    arr.append(left[i])
                    i += 1
                    continue
                    
                if left[i][0] >= right[j][0]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            return arr
        merge_sort(0, len(nums) - 1)
        return result         
            
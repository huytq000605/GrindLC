class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def ms(start, end):
            if start == end:
                return [nums[start]]
            mid = start + (end - start) // 2
            left = ms(start, mid)
            right = ms(mid+1, end)
            i, j = 0, 0
            m, n = len(left), len(right)
            s = []
            while i + j < m+n:
                if i < m and j < n:
                    if left[i] <= right[j]:
                        s.append(left[i])
                        i += 1
                    else:
                        s.append(right[j])
                        j += 1
                elif i < m:
                    s.append(left[i])
                    i += 1
                else:
                    s.append(right[j])
                    j += 1
            return s
        return ms(0, len(nums) - 1)

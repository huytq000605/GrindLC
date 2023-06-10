class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        def valid(num):
            # [0, index -1]
            # num - 1
            # num - index
            left = ((num-1) + (num-index)) * (index) // 2
            # [index+1, n-1]
            # num-1
            # num-(n-1-index)
            right = ((num-n+1+index) - (num-1)) * (n-1-index) // 2
            if left + right + num > max_sum:
                return False
            return True
        start = 1
        end = max_sum
        while start < end:
            mid = start + math.ceil((end - start + 1) // 2)
            if valid(mid):
                start = mid
            else:
                end = mid - 1
        return start

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = []
        for s in strs:
            ones = 0
            zeros = 0
            for l in s:
                if l == "0":
                    zeros += 1
                else:
                    ones += 1
            arr.append((ones, zeros))
        @cache
        def dfs(i, ones, zeros):
            if i >= len(arr):
                return 0
            result = dfs(i+1, ones, zeros)
            next_ones = ones + arr[i][0]
            next_zeros = zeros + arr[i][1]
            if next_ones <= n and next_zeros <= m:
                result = max(result, dfs(i + 1, next_ones, next_zeros) + 1)
            return result
        return dfs(0, 0, 0)
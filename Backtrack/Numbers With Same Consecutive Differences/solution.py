class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def dfs(num, length):
            nonlocal result
            if length == n:
                result.append(num)
                return
            last = num % 10
            for i in range(10):
                if abs(last - i) == k:
                    dfs(num * 10 + i, length + 1)
        for i in range(1, 10):
            dfs(i, 1)
        return result

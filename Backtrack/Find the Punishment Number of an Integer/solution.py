class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        def valid(num):
            target = num
            num = str(num**2)
            n = len(num)
            def dfs(i, cur):
                if i >= n:
                    if cur == target: return True
                    return False
                for j in range(i, n):
                    if dfs(j + 1, cur + int(num[i:j+1])):
                        return True
                return False
            return dfs(0, 0)
            
        for num in range(n+1):
            if valid(num):
                result += num ** 2
        return result

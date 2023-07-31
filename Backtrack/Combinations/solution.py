class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur = []
        result = []
        def dfs(num):
            if len(cur) == k:
                result.append([*cur])
                return
            for next_num in range(num, n+1):
                cur.append(next_num)
                dfs(next_num+1)
                cur.pop()
        dfs(1)
        return result

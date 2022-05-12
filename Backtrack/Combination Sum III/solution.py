class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def dfs(num, total, cur):
            nonlocal result
            if total == n and len(cur) == k:
                result.append([*cur])
                return
            if num == 0 or total > n or len(cur) >= k:
                return
            cur.append(num)
            dfs(num-1, total + num, cur)
            cur.pop()
            dfs(num-1, total, cur)
            
        dfs(9, 0, [])
        return result
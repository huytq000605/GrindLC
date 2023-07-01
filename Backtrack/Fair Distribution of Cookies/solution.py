class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        states = [0 for i in range(k)]
        cookies.sort(reverse = True)
        ans = math.inf
        def dfs(i):
            nonlocal states, ans
            if i >= len(cookies):
                result = max(states)
                ans = min(ans, result)
                return result
            if max(states) >= ans:
                return math.inf
            result = math.inf
            for j in range(k):
                states[j] += cookies[i]
                result = min(result, dfs(i + 1))
                states[j] -= cookies[i]
            return result
        return dfs(0)

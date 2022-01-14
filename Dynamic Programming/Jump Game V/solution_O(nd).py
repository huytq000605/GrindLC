class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def dfs(idx):
            result = 0
            for i in range(1, d + 1):
                next_idx = idx - i
                if next_idx < 0 or arr[idx] <= arr[next_idx]:
                    break
                result = max(result, 1 + dfs(next_idx))
            
            for i in range(1, d+1):
                next_idx = idx + i
                if next_idx >= n or arr[idx] <= arr[next_idx]:
                    break
                result = max(result, 1 + dfs(next_idx))
            return result
        
        result = 0
        for i in range(n):
            result = max(result, 1 + dfs(i))
        return result

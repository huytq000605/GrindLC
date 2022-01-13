class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        result = []
        n = len(arr)
        def dfs(idx, current):
            nonlocal result
            if idx >= n:
                result.append([*current])
                return
            
            for i in range(idx, n):
                arr[idx], arr[i] = arr[i], arr[idx]
                current.append(arr[idx])
                dfs(idx + 1, current)
                current.pop()
                arr[idx], arr[i] = arr[i], arr[idx]
        
        dfs(0, [])
        return result

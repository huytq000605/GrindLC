class Solution:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        result = []
        n = len(arr)
        def dfs(idx, current):
            nonlocal result
            if idx >= n:
                result.append([*current])
                return
            seen = set()
            for i in range(idx, n):
                if arr[i] in seen:
                    continue
                arr[idx], arr[i] = arr[i], arr[idx]
                current.append(arr[idx])
                seen.add(arr[idx])
                dfs(idx + 1, current)
                current.pop()
                arr[idx], arr[i] = arr[i], arr[idx]
        
        dfs(0, [])
        return result

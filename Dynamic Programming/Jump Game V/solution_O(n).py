class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        next_higher = [n for i in range(n)]
        prev_higher = [n for i in range(n)]
        
        stack = []
        for i in range(n):
            while len(stack) > 0 and i - stack[-1] <= d and arr[i] > arr[stack[-1]]:
                next_higher[stack.pop()] = i
            stack.append(i)
        
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1] - i <= d and arr[i] > arr[stack[-1]]:
                prev_higher[stack.pop()] = i
            stack.append(i)
            
        @cache
        def dfs(idx):
            if idx >= n:
                return -1
            return max(1 + dfs(next_higher[idx]), 1 + dfs(prev_higher[idx]))
        result = 0
        for i in range(n):
            result = max(result, 1 + dfs(i))
        
        return result

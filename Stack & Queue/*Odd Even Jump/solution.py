class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher = [n for i in range(n)]
        next_lower = [n for i in range(n)]
        
        stack = []
        for a, i in sorted([(a, i) for i, a in enumerate(arr)]):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for a, i in sorted([(-a, i) for i, a in enumerate(arr)]):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
                
        @cache
        def dfs(i, odd):
            if i == n:
                return False
            if i == n-1:
                return True
            if odd:
                return dfs(next_higher[i], False)
            else:
                return dfs(next_lower[i], True)
        
        result = 0
        for i in range(n):
            if dfs(i, True):
                result += 1
        
        return result
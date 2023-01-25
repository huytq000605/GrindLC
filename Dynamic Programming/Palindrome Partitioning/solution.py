class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        result = []
        partition = []
        n = len(s)
        def dfs(i):
            if i >= n:
                result.append([*partition])
            for j in range(i, n):
                if is_palindrome(i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return result
            

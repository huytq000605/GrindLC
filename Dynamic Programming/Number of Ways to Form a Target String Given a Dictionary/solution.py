class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        arr = [[0 for j in range(26)] for i in range(len(words[0]))]
        for i in range(len(words[0])):
            for j in range(len(words)):
                letter = words[j][i]
                arr[i][ord(letter) - ord('a')] += 1

        @cache
        def dfs(i, j):
            if j >= len(target):
                return 1
            if i >= len(words[0]):
                return 0
            result = arr[i][ord(target[j]) - ord('a')] * dfs(i + 1, j + 1)
            result += dfs(i + 1, j)
            return result % (10**9 + 7)
        
        return dfs(0, 0)

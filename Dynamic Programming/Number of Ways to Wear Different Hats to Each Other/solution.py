class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        wearable = [[0 for j in range(40)] for i in range(n)]
        for person, can_wear in enumerate(hats):
            for hat in can_wear:
                wearable[person][hat-1] = 1
            
        @cache
        def dfs(i, people):
            if people == 0:
                return 1
            if i >= 40:
                return 0
            result = 0
            for j in range(n):
                if (people >> j) & 1:
                    if wearable[j][i]:
                        result += dfs(i + 1, people & ~(1 << j))
            result += dfs(i+1, people)
            return result % (10**9 + 7)
        
        return dfs(0, (1<<n) - 1)
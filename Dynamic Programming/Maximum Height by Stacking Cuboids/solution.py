class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for i in range(n):
            cuboids[i].sort()
        cuboids.sort(key = lambda cuboid: (cuboid[2], cuboid[1], cuboid[0]))

        @cache
        def dfs(i, prev):
            if i >= n:
                return 0
            valid = True
            for j in range(3):
                if cuboids[i][j] < cuboids[prev][j]:
                    valid = False
            result = 0
            if valid:
                result = dfs(i + 1, i) + cuboids[i][2]
            result = max(result, dfs(i+1, prev))
            return result
        
        result = 0
        for i in range(n):
            result = max(result, dfs(i + 1, i) + cuboids[i][2])
        return result

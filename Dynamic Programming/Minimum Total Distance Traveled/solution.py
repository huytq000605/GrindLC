class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        @cache
        def dfs(i, j, k):
            if i >= len(robot):
                return 0
            if j >= len(factory):
                return math.inf
            result = dfs(i, j+1, 0)
            if k < factory[j][1]:
                result = min(result, dfs(i+1, j, k+1) + abs(factory[j][0] - robot[i]))
            return result
        return dfs(0, 0, 0)
            
            

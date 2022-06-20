class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        position = defaultdict(list)
        for i, l in enumerate(ring):
            position[l].append(i)
        
        @cache
        def dfs(i, j):
            nonlocal position
            if j >= len(key):
                return 0
            result = math.inf
            l = key[j]
            pos = bisect.bisect_left(position[l], i)
            m = len(position[l])
            for k in range(-1, 2):
                next_position = position[l][(pos+k)%m]
                result = min(result, min(n - abs(next_position-i), abs(next_position-i)) + dfs(next_position, j+1))
            return result
        return dfs(0, 0) + len(key)
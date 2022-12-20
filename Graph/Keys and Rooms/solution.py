class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = [0 for i in range(n)]
        seen[0] = 1
        def dfs(u):
            for v in rooms[u]:
                if not seen[v]:
                    seen[v] = 1
                    dfs(v)
        dfs(0)
        if sum(seen) == n:
            return True
        return False

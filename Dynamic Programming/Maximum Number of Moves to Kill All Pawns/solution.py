class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)
        positions.append([kx, ky])
        dp = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
        ds = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]

        for p in range(n+1):
            r, c = positions[p]
            dp[p][p] = 0
            q = deque([(0, r, c)])
            seen = set([(r, c)])
            while q:
                s, r, c = q.popleft()
                for p2 in range(n):
                    if [r, c] == positions[p2]:
                        dp[p][p2] = s
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= 50 or nc < 0 or nc >= 50: continue
                    if (nr, nc) in seen: continue
                    seen.add((nr, nc))
                    q.append((s+1, nr, nc))

        @cache
        def dfs(p, mask, player):
            if mask == 2**n - 1: return 0
            print(mask)
            if player == 0:
                result = 0
                for p2 in range(n):
                    bit_mask = 1 << p2
                    if mask & bit_mask: continue
                    result = max(result, dp[p][p2] + dfs(p2, mask | bit_mask, 1 - player))
            else:
                result = 50*50
                for p2 in range(n):
                    bit_mask = 1 << p2
                    if mask & bit_mask: continue
                    result = min(result, dp[p][p2] + dfs(p2, mask | bit_mask, 1 - player))
            return result
        
        return dfs(n, 0, 0)

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def convert(l):
            s = ""
            for num in l:
                s += str(num)
                s += "#"
            return s
        
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dq = deque([([grid[i // 3][i % 3] for i in range(9)], 0)])
        seen = set()
        seen.add(convert(dq[0]))

        while dq:
            state, s = dq.popleft()

            valid = True
            for i in range(9):
                if state[i] < 1:
                    valid = False
                    break
            if valid: return s
            
            for r in range(3):
                for c in range(3):
                    if state[r * 3 + c] <= 1:
                        continue
                    for dr, dc in ds:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= 3 or nc >= 3:
                            continue
                        next_state = [*state]
                        next_state[nr * 3 + nc] += 1
                        next_state[r * 3 + c] -= 1
                        key = convert(next_state)
                        if key not in seen:
                            seen.add(key)
                            dq.append((next_state, s+1))
        return -1
            
            
            

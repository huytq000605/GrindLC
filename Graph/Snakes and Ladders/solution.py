class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_rc(idx):
            r = idx // n
            c = idx % n
            r = n-1-r
            if (n-1-r) % 2 == 1:
                c = n-1-c
            return r, c
        
        def get_idx(r, c):
            if (n-1-r) % 2 == 1:
                return (n-1-r) * n + (n-1-c)
            return (n-1-r) * n + c
        
        goal = n*n-1
        q = deque([(0, 0)])
        while q:
            idx, s = q.popleft()
            r, c = get_rc(idx)
            if idx == goal:
                return s
            for nxt in range(idx + 1, min(idx + 7, n * n)):
                nr, nc = get_rc(nxt)
                if board[nr][nc] == -2:
                    continue
                if board[nr][nc] != -1:
                    nxt = board[nr][nc] - 1
                board[nr][nc] = -2
                q.append((nxt, s+1))
        return -1
            

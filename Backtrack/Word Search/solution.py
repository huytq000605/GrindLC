class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
        m, n, k = len(board), len(board[0]), len(word)
        if k > m * n:
            return False
        counter = Counter(word)
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]
        
        def dfs(r, c, i):
            if i == k-1:
                return True
            tmp = board[r][c]
            board[r][c] = "#"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n or board[nr][nc] != word[i+1]:
                    continue
                if dfs(nr, nc, i+1):
                    return True
            board[r][c] = tmp
            return False
        
        for r in range(m):
            for c in range(n):
                if word[0] == board[r][c] and dfs(r, c, 0):
                    return True
        return False
            

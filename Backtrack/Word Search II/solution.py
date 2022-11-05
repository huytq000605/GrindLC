class Solution(object):
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        trie = dict()
        result = []
        ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            cur["word"] = word

        def dfs(r, c, cur):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] not in cur:
                return
            letter = board[r][c]
            cur = cur[letter]
            board[r][c] = "#"
            if "word" in cur:
                result.append(cur["word"])
                del cur["word"]
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, cur)
            board[r][c] = letter
            
        for r in range(m):
            for c in range(n):
                dfs(r, c, trie)
        return result
                    
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def add_to_trie(trie, word):
            current = trie
            for l in word:
                if l not in current:
                    current[l] = {}
                current = current[l]
            current["is_word"] = True
            current["word"] = word
        
        trie = {}
        for word in words:
            add_to_trie(trie, word)
        m, n = len(board), len(board[0])
        dirs = [(0,1), (1,0), (-1, 0), (0, -1)]
        result = []
        def dfs(r, c, current):
            nonlocal result
            if "is_word" in current and current["is_word"] == True:
                current["is_word"] = False
                result.append(current["word"])
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or board[nr][nc] == "#" or board[nr][nc] not in current:
                    continue
               letter = board[nr][nc]
                board[nr][nc] = "#"
                dfs(nr, nc, current[letter])
                board[nr][nc] = letter
        
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter in trie:
                    board[i][j] = "#"
                    dfs(i, j, trie[letter])
                    board[i][j] = letter
                    
        
        return result

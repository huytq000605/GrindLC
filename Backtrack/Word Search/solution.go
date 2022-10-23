func exist(board [][]byte, word string) bool {
    dirs := [][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}
    m, n := len(board), len(board[0])
    var dfs func(r, c, i int) bool
    dfs = func(r, c, i int) bool {
        if i == len(word) - 1 {
           return true 
        }
        for _, d := range dirs {
            nr, nc := r + d[0], c + d[1]
            if nr < 0 || nc < 0 || nr >= m || nc >= n || board[nr][nc] != word[i+1] {
                continue
            }
            tmp := board[nr][nc]
            board[nr][nc] = '#'
            if dfs(nr, nc, i+1) {
                return true
            }
            board[nr][nc] = tmp
        }
        return false
    }
    
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if board[r][c] == word[0] {
                tmp := board[r][c]
                board[r][c] = '#'
                if dfs(r, c, 0) {
                    return true
                }
                board[r][c] = tmp
            }
        }
    }
    return false
}

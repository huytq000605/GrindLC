package main

func maxAreaOfIsland(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    type dir [2]int
    dirs := [4]dir{dir{0, 1}, dir{1, 0}, dir{-1, 0}, dir{0, -1}}
    result := 0

    var dfs func(int, int) int
    dfs = func(r, c int) int {
        result := 1
        for _, d := range dirs {
            dr, dc := d[0], d[1]
            nr, nc := r + dr, c + dc
            if nr < 0 || nc < 0 || nr >= m || nc >= n || grid[nr][nc] == 0 {
                continue
            }
            grid[nr][nc] = 0
            result += dfs(nr, nc)
        }
        return result
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                grid[i][j] = 0
                ret := dfs(i, j)
                if ret > result {
                    result = ret 
                }
            }
        }
    }
    return result
}


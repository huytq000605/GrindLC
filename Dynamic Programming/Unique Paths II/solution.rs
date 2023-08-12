impl Solution {
    pub fn unique_paths_with_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][0] == 1 { return 0 }
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp = vec![vec![0; n+1]; m+1];
        dp[1][1] = 1;
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 { continue }
                dp[r+1][c+1] += dp[r][c+1] + dp[r+1][c];
            }
        }
        return dp[m][n]
    }
}

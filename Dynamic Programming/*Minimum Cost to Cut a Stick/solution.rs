impl Solution {
    pub fn min_cost(n: i32, mut cuts: Vec<i32>) -> i32 {
        cuts.append(&mut vec![0, n]);
        cuts.sort();
        let m = cuts.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![std::i32::MAX; m]; m];
        for d in 1 as usize..m {
            for i in 0..m - d {
                if d == 1 {
                    dp[i][i+d] = 0;
                }
                for k in 1..d {
                    dp[i][i+d] = std::cmp::min(dp[i][i+d], cuts[i+d] - cuts[i] + dp[i][i+k] + dp[i+k][i + d]);   
                }
            }
        }
        return dp[0][m-1] as i32
    }
}

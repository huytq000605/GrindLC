impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let mut dp = vec![vec![0; s2.len() + 1]; s1.len() + 1];
        let (s1, s2) = (s1.as_bytes(), s2.as_bytes());
        dp[s1.len()][s2.len()] = 0;
        for i in (0..s2.len()).rev() {
            dp[s1.len()][i] = dp[s1.len()][i+1] + s2[i] as i32;
        }
        for i in (0..s1.len()).rev() {
            dp[i][s2.len()] = dp[i+1][s2.len()] + s1[i] as i32
        }
        // dp[i][j] = min(dp[i][j+1] + s2[j], dp[i+1][j] + s1[i])
        for i in (0..s1.len()).rev() {
            for j in (0..s2.len()).rev() {
                if s1[i] == s2[j] {
                    dp[i][j] = dp[i+1][j+1];
                } else {
                    dp[i][j] = std::cmp::min(
                        dp[i][j+1] + s2[j] as i32,
                        dp[i+1][j] + s1[i] as i32
                    )
                }
            }
        }
        return dp[0][0]
    }
}

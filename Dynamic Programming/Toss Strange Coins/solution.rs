impl Solution {
    pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
        let n = prob.len();
        let mut dp = vec![vec![0.0; (target + 1) as usize]; n+1];
        dp[0][0] = 1.0;
        for i in 0..n {
            for j in 0..target+1 {
                let (iu, ju) = (i as usize, j as usize);
                if ju > 0 {
                    dp[iu+1][ju] += dp[iu][ju-1] * prob[iu];
                }
                dp[iu+1][ju] += dp[iu][ju] * (1.0 - prob[iu]);
            }
        }
        return dp[n][target as usize]
    }
}

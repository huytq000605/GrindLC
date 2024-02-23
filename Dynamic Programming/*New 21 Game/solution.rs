impl Solution {
    pub fn new21_game(n: i32, k: i32, w: i32) -> f64 {
        if k == 0 || k + w < n {
            return 1.0;
        }
        let mut dp = vec![0 as f64; (n+1) as usize];
        dp[0] = 1.0;
        let mut s = 1.0;
        for i in 1..n+1 {
            dp[i as usize] = s * 1.0 / w as f64;
            if i < k {
                s += dp[i as usize];
            }
            if i >= w {
                s -= dp[(i-w) as usize];
            }
        }
        return dp[k as usize..(n+1) as usize].iter().sum();
    }
}

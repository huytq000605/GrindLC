impl Solution {
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
        let mut dp = vec![n+2; n as usize + 2];
        dp[0] = 0;
        for (i, &r) in ranges.iter().enumerate() {
            let (start, end) = (std::cmp::max(0, i as i32 - r), std::cmp::min(i as i32 + r, n));
            for j in start..end + 1 {
                dp[j as usize + 1] = std::cmp::min(dp[j as usize + 1], dp[start as usize] + 1);
            }
        }
        if dp[n as usize + 1] == n+2 {
            return -1
        }
        return dp[n as usize + 1]
    }
}

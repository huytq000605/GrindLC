impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut n = n as usize;
        let mut dp = vec![0; n+1];
        for i in 1..n+1 {
            dp[i] = (i as i32 & 1) + dp[i>>1]
        }
        return dp
    }
}

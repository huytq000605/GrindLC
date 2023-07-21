impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // dp[i][0] = longest_length until nums[i]
        // dp[i][1] = count until nums[i]
        let mut dp = vec![vec![0; 2]; n];
        let mut max_len = 0;
        let mut result = 0;
        for i in 0..n {
            dp[i] = vec![1, 1];
            for j in 0..i {
                if nums[j] < nums[i] {
                    if dp[j][0] + 1 > dp[i][0] {
                        dp[i][0] = dp[j][0] + 1;
                        dp[i][1] = dp[j][1];
                    } else if dp[j][0] + 1 == dp[i][0] {
                        dp[i][1] += dp[j][1];
                    }
                }
            }
            
            if dp[i][0] > max_len {
                max_len = dp[i][0];
                result = dp[i][1];
            } else if dp[i][0] == max_len {
                result += dp[i][1];
            }
        }
        result
    }
}

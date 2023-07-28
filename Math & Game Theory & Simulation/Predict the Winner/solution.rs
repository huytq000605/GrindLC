impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![vec![10_000_000; n]; n];
        fn dfs(nums: &Vec<i32>, dp: &mut Vec<Vec<i32>>, i: i32, j: i32) -> i32 {
            if j < 0 || i > j {
                return 0
            }
            let (i, j) = (i as usize, j as usize);
            if dp[i][j] != 10_000_000 {
                return dp[i][j]
            }
            dp[i][j] = std::cmp::max(nums[i] - dfs(nums, dp, i as i32+1, j as i32), nums[j] - dfs(nums, dp, i as i32, j as i32 -1));
            return dp[i][j]
        }
        return dfs(&nums, &mut dp, 0, n as i32 - 1) >= 0
    }
}

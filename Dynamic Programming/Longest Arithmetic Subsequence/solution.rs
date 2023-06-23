use std::collections::HashMap;

impl Solution {
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = Vec::<HashMap<i32, i32>>::new();
        for _ in 0..n {
            dp.push(HashMap::<i32, i32>::new());
        }
        let mut result = 0;
        
        for i in 0..n {
            for j in 0..i {
                let diff = nums[i] - nums[j];
                let previous_value = *dp[j].get(&diff).or_else(|| Some(&1)).unwrap();
                dp[i].insert(diff, previous_value + 1);
                result = std::cmp::max(result, *dp[i].get(&diff).unwrap());
            }
        }
        result
    }
}

use std::collections::HashSet;

impl Solution {
    pub fn permute_unique(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let mut current = vec![];
        let n = nums.len();
        fn dfs(i: usize, current: &mut Vec<i32>, result: &mut Vec<Vec<i32>>, n: usize, nums: &mut Vec<i32>) {
            if current.len() == n {
                result.push(current.clone());
            }
            if i >= n {
                return
            }
            let mut seen = HashSet::new();
            for j in i..n {
                if !seen.contains(&nums[j]) {
                    seen.insert(nums[j]);
                    current.push(nums[j]);
                    nums.swap(i, j);
                    dfs(i + 1, current, result, n, nums);
                    nums.swap(i, j);
                    current.pop();
                }
            }
        }
        dfs(0, &mut current, &mut result, n, &mut nums);
        return result
    }
}
impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut result = vec![-1; nums.len()];
        let mut s: i64 = 0;
        for i in 0..std::cmp::min(2*k as usize, nums.len()) {
            s += nums[i] as i64;
        }
        for i in 2*k as usize..nums.len() {
            s += nums[i] as i64;
            result[i - k as usize] = (s / (2*k as i64+1)) as i32;
            s -= nums[i - 2*k as usize] as i64;
        }
        return result
    }
}

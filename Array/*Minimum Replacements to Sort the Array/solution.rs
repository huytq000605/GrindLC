impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let mut mx = nums[nums.len() - 1];
        let mut result = 0;
        for i in (0..nums.len() - 1).rev() {
            let parts = (nums[i] as f64 / mx as f64).ceil() as i64;
            result += parts - 1;
            mx = nums[i] / parts as i32;
        }
        return result
    }
}

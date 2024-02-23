impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i64 {
        let mut result: i64 = 0;
        let mut j = 0;
        for i in 0..nums.len() {
            if i > 0 && nums[i] <= nums[i-1] {
                j = i
            }
            result += (i - j + 1) as i64
        }
        return result
    }
}

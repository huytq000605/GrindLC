impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let (mut result, mut prev, mut cur) = (0,0,0);
        for &num in nums.iter() {
            if num == 0 {
                prev = cur;
                cur = 0;
            } else {
                cur += 1;
                result = std::cmp::max(result, prev + cur);
            }
        }
        return std::cmp::min(result, nums.len() as i32 - 1)
    }
}

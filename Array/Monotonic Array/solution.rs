impl Solution {
    pub fn is_monotonic(nums: Vec<i32>) -> bool {
        let (mut increasing, mut decreasing) = (false, false);
        for i in 1..nums.len() {
            if nums[i] < nums[i-1] {
                increasing = true;
            }
            if nums[i] > nums[i-1] {
                decreasing = true;
            }
        }
        if increasing && decreasing { return false }
        return true
    }
}

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        fn at_most(nums: &Vec<i32>, k: i32) -> i32 {
            if k < 0 {
                return 0
            }
            let (mut j, mut result, mut s) = (0 as usize, 0, 0);
            for i in 0..nums.len() {
                s += nums[i];
                while s > k {
                    s -= nums[j];
                    j += 1;
                }
                result += (i - j + 1);
            }
            return result as i32
        }
        return at_most(&nums, goal) - at_most(&nums, goal-1);
    }
}

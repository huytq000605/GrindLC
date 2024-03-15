impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut result = vec![1; n];
        let mut cur = 1;
        for i in 0..n {
            result[i] *= cur;
            cur *= nums[i];
        }
        cur = 1;
        for i in (0..n).rev() {
            result[i] *= cur;
            cur *= nums[i];
        }
        return result
    }
}

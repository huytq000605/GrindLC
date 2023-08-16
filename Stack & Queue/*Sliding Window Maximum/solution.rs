impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        use std::collections::VecDeque;
        let mut dq = VecDeque::new();
        let mut result = vec![0; nums.len() - k + 1];
        for (i, &num) in nums.iter().enumerate() {
            if dq.len() > 0 && i - dq[0] >= k {
                dq.pop_front();
            }
            while dq.len() > 0 && nums[dq[dq.len() - 1]] <= num {
                dq.pop_back();
            }
            dq.push_back(i);
            if i >= k-1 {
                result[i - k + 1] = nums[dq[0]]
            }
        }
        result
    }
}

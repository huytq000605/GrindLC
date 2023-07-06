impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let (mut result, mut sum, mut start) = (i32::MAX, 0, 0 as usize);
        for (i, &num) in nums.iter().enumerate() {
            sum += num;
            while sum - nums[start] >= target {
                sum -= nums[start];
                start += 1;
            }
            if sum >= target {
                result = std::cmp::min(result, (i - start + 1) as i32);
            }
        }
        if result == i32::MAX {
            return 0
        }
        result
    }
}

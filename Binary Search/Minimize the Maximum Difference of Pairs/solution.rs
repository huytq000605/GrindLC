impl Solution {
    pub fn minimize_max(mut nums: Vec<i32>, p: i32) -> i32 {
        nums.sort();
        if nums.len() == 0 {
            return 0
        }
        fn valid(nums: &Vec<i32>, p: i32, threshold: i32) -> bool {
            let mut i: usize = 0;
            let mut k = 0;
            while i < nums.len() {
                if i + 1 >= nums.len() { break }
                if (nums[i] - nums[i+1]).abs() <= threshold {
                    i += 2;
                    k += 1
                } else {
                    i += 1;
                }
            }
            return k >= p
        }
        let (mut start, mut end) = (0, nums[nums.len() - 1] - nums[0]);
        while start < end {
            let mid = start + (end - start) / 2;
            if valid(&nums, p, mid) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start
    }
}

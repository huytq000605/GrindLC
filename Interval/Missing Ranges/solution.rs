impl Solution {
    pub fn find_missing_ranges(nums: Vec<i32>, lower: i32, upper: i32) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let mut missing = lower;
        for &num in nums.iter() {
            if num == missing {
                missing += 1;
            } else {
                result.push(vec![missing, num - 1]);
                missing = num + 1;
            }
        }
        if missing <= upper {
            result.push(vec![missing, upper]);
        }
        return result
    }
}

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.len() == 0 {
            return vec![]
        }
        if nums.len() == 1 {
            return vec![format!("{}", nums[0])]
        }
        let mut ranges: Vec<(i32, i32)> = vec![(nums[0], nums[0])];
        for &num in &nums[1..] {
            if num as i64 - ranges.last().unwrap().1 as i64 <= 1 {
                ranges.last_mut().unwrap().1 = num;
            } else {
                ranges.push((num, num));
            }
        }
        let mut result = vec![];
        for (a, b) in ranges {
            if a < b {
                result.push(format!("{}->{}", a, b));
            } else {
                result.push(format!("{}", a));
            }
        }
        return result
    }
}

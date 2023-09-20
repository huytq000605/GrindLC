impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let target: i32 = nums.iter().sum::<i32>() - x;
        let mut result = i32::MAX;
        let mut seen = std::collections::HashMap::<i32, i32>::new();
        seen.insert(0, -1);
        let mut s = 0;
        let n = nums.len() as i32;
        for (i, num) in nums.iter().enumerate() {
            let i = i as i32;
            s += num;
            if !seen.contains_key(&s) {
                seen.insert(s, i);
            }
            if seen.contains_key(&(s - target)) {
                result = std::cmp::min(result, n - (i - seen.get(&(s - target)).unwrap()));
            }
        }
        if result == i32::MAX {
            return -1
        }
        return result
    }
}

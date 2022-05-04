use std::collections::HashMap;

impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut map = HashMap::<i32, i32>::new();
        let mut result = 0;
        for num in &nums {
            let remain = k - num;
            let freq_remain = match map.get(&remain) {
                Some(freq) => *freq,
                None => 0
            };
            if freq_remain > 0 {
                map.insert(k - num, freq_remain - 1);
                result += 1;
            } else {
                let mut freq = map.entry(*num).or_insert(0);
                *freq += 1;
            }
        }
        return result;
    }
}
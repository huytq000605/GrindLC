impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap;
        let at_most = |k: i32| -> i32 {
            let (mut start, mut result, mut counter) = (0, 0, HashMap::<i32, i32>::new());
            for (i, &num) in nums.iter().enumerate() {
                *counter.entry(num).or_insert(0) += 1;
                while counter.len() > k as usize {
                    let mut count = counter.get_mut(&nums[start]).unwrap();
                    *count -= 1;
                    if *count == 0 { counter.remove(&nums[start]); };
                    start += 1;
                }
                result += (i - start + 1);
            }
            result as i32
        };
        at_most(k) - at_most(k-1)
    }
}

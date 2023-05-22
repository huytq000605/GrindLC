use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut pq = BinaryHeap::new();
        let mut hm = HashMap::new();
        for &num in nums.iter() {
            let freq = hm.entry(num).or_insert(0);
            *freq += 1;
        }
        for (num, freq) in hm.iter() {
            pq.push((-freq, num));
            if pq.len() as i32 > k {
                pq.pop();
            }
        }
        let mut result = vec![];
        while pq.len() > 0 {
            result.push(*pq.pop().unwrap().1);
        }
        return result

    }
}

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::BinaryHeap;
        let mut pq = BinaryHeap::new();
        for num in nums {
            pq.push(-num);
            if pq.len() > k as usize {
                pq.pop();
            }
        }
        return -pq.pop().unwrap()
    }
}

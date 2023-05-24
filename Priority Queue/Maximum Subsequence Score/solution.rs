impl Solution {
    pub fn max_score(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let n = nums1.len();
        let mut nums: Vec<(i32, i32)> = nums1.iter().
            zip(nums2.iter()).
            map(|(num1, num2)| (*num1, *num2)).
            collect();
        nums.sort_by(|a, b| b.1.cmp(&a.1));
        let mut pq = std::collections::BinaryHeap::new();
        let (mut s, mut result) = (0 as i64, 0 as i64);
        for (num, mul) in nums {
            pq.push(-num);
            s += num as i64;
            if pq.len() > k as usize {
                s += pq.pop().unwrap() as i64;
            }
            if pq.len() == k as usize {
                result = std::cmp::max(result, mul as i64 * s)
            }
        }
        return result as i64
    }
}

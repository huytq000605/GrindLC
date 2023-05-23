use std::collections::{BinaryHeap};

impl Solution {
    pub fn min_meeting_rooms(mut intervals: Vec<Vec<i32>>) -> i32 {
        let mut pq = BinaryHeap::new();
        intervals.sort();
        let mut result = 0;
        for interval in intervals {
            let [s1, s2] = match &interval[..] {
                [a, b] => [*a, *b],
                _ => [-1, -1]
            };
            while pq.len() > 0 && -pq.peek().unwrap() <= s1 {
                pq.pop();
            }
            pq.push(-s2);
            result = std::cmp::max(result, pq.len());
        }
        return result as i32
    }
}

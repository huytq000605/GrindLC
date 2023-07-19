impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        let mut result = 0;
        intervals.sort();
        let mut prev = intervals[0][0]-1;
        for interval in intervals {
            let (a, b) = match &interval[..] {
                &[a, b] => (a, b),
                _ => panic!("Panicked")
            };
            if a < prev {
                result += 1;
                prev = std::cmp::min(prev, b);
            } else {
                prev = b;
            }
        }
        result
    }
}

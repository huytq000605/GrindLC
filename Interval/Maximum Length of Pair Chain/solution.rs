impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        pairs.sort_by(|a, b| {
            use  std::cmp::Ordering;
            if a[0].cmp(&b[0]) == Ordering::Equal {
                return a[1].cmp(&b[1])
            }
            return a[0].cmp(&b[0])
        });
        let mut result = 0;
        let mut prev = i32::MIN;
        for pair in pairs.iter() {
            if let [s, e] = pair[..] {
                if s > prev {
                    prev = e;
                    result += 1;
                } else {
                    prev = std::cmp::min(prev, e);
                }
            }
        }
        return result
    }
}

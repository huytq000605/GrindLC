impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let (mut result, mut start, mut t, mut f) = (0, 0 as usize, 0, 0);
        let bs = answer_key.as_bytes();
        for (i, &b) in bs.iter().enumerate() {
            if b == 'T' as u8 {
                t += 1;
            } else {
                f += 1;
            }
            while std::cmp::min(t, f) > k {
                if bs[start] == 'T' as u8 {
                    t -= 1;
                } else {
                    f -= 1;
                }
                start += 1;
            }
            result = std::cmp::max(result, (i - start + 1) as i32);
        }
        return result
    }
}

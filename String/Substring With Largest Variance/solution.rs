impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        let mut counter = vec![0; 26];
        let s = s.as_bytes();
        let mut chars = std::collections::HashSet::new();
        for &c in s.iter() {
            counter[(c as u8 - 'a' as u8) as usize] += 1;
            chars.insert(c);
        }
        let mut result = 0;
        for &c1 in chars.iter() {
            for &c2 in chars.iter() {
                if c1 == c2 { continue }
                let (mut count_c1, mut count_c2, mut remain_c2) = (0, 0, counter[(c2 as u8 - 'a' as u8) as usize]);
                for &c in s.iter() {
                    if c == c1 { count_c1 += 1; }
                    if c == c2 { 
                        count_c2 += 1;
                        remain_c2 -= 1; 
                    }
                    if count_c2 > count_c1 && remain_c2 > 0 {
                        count_c1 = 0;
                        count_c2 = 0;
                    }
                    if count_c2 > 0 {
                        result = std::cmp::max(result, count_c1 - count_c2);
                    }
                }
            }
        }
        return result
    }
}

impl Solution {
    pub fn length_of_longest_substring_two_distinct(s: String) -> i32 {
        let mut d = std::collections::HashMap::<u8, i32>::new();
        let mut j = 0;
        let s = s.as_bytes();
        let mut result = 0;
        for (i, &c) in s.iter().enumerate() {
            d.entry(c).and_modify(|e| { *e += 1 }).or_insert(1);
            while d.len() > 2 {
                d.entry(s[j]).and_modify(|e| { *e -= 1 });
                if *d.get(&s[j]).unwrap() == 0 {
                    d.remove(&s[j]);
                }
                j += 1;
            }
            result = std::cmp::max(result, i - j + 1);
        }
        return result as i32
    }
}

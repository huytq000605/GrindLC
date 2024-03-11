impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut counter = vec![0; 26];
        for c in s.into_bytes() {
            counter[(c - 'a' as u8) as usize] += 1;
        }
        let mut result = vec![];
        for c in order.into_bytes() {
            while counter[(c - 'a' as u8) as usize] > 0 {
                result.push(c);
                counter[(c - 'a' as u8) as usize] -= 1;
            }
        }
        for i in 0..26 {
            while counter[i] > 0 {
                result.push(i as u8 + 'a' as u8);
                counter[i] -= 1;
            }
        }
        return String::from_utf8(result).unwrap()
    }
}

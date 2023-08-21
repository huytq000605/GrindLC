impl Solution {
    pub fn convert_to_title(mut n: i32) -> String {
        let mut result = "".to_owned();
        while n > 0 {
            n -= 1;
            let chr = &vec![(n % 26) as u8 + 'A' as u8];
            let ss = std::str::from_utf8(chr).expect(":D");
            result += ss;
            n /= 26;
        }
        return result.chars().rev().collect()
    }
}

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut xor = 0;
        for b in s.as_bytes() {
            xor ^= b;
        }
        for b in t.as_bytes() {
            xor ^= b;
        }
        return xor as char
    }
}

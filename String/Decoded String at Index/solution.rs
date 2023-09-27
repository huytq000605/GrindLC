impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        let mut i = -1;
        let mut length: i64 = 0;
        let s = s.as_bytes();
        let k = k as i64;
        let RADIX = 10;
        for &b in s.iter() {
            let c = b as char;
            if c.is_digit(RADIX) {
                length *= c.to_digit(RADIX).unwrap() as i64;
            } else {
                length += 1;
            }
            i += 1;
            if length >= k {
                break
            }
        }
        
        let mut k = k-1;
        loop {
            let c = s[i as usize] as char;
            if c.is_digit(RADIX) {
                length /= c.to_digit(RADIX).unwrap() as i64;
                k %= length;
            } else {
                if k == length - 1 {
                    return (s[i as usize] as char).to_string()
                }
                length -= 1;
            }
            
            i -= 1;
        }
        return "".to_string()
    }
}

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let bs = s.as_bytes();
        for i in 1..s.len() / 2 + 1 {
            if s.len() % i != 0 { continue }
            let ss = &bs[0..i];
            let mut valid = true;
            for j in 0..s.len() {
                if ss[j % ss.len()] != bs[j] {
                    valid = false;
                    break
                }
            }
            
            if valid {
                return true
            }
        }
        return false
    }
}

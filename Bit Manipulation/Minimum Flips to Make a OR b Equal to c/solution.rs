impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut result = 0;
        for i in 0..30 {
            if (c >> i) & 1 == 0 {
                if (a >> i) & 1 == 1 {
                    result += 1;
                }
                if (b >> i) & 1 == 1 {
                    result += 1;
                }
            } else {
                if ((a >> i) | (b >> i)) & 1 == 0 {
                    result += 1;
                }
            }
        }
        return result
    }
}

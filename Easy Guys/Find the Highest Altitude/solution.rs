impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let (mut result, mut s) = (0, 0);
        for g in gain {
            s += g;
            result = std::cmp::max(result, s);
        }
        result
    }
}

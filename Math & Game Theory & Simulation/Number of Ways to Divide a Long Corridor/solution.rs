impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        const MOD:i64 = 1_000_000_000 + 7;
        let mut total_s = 0;
        let (mut s, mut p, mut result) = (0, 1, 1 as i64);
        for c in corridor.chars() {
            if c == 'S' {
                total_s += 1;
                if s == 2 {
                    result = (result * p) % MOD;
                    p = 1;
                    s = 0;
                }
                s += 1;
            } else if s == 2 {
                p += 1;
            }
        }
        if total_s % 2 == 1 || total_s == 0 {
            return 0
        }
        return result as i32
    }
}

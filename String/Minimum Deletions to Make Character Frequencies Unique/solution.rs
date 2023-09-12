impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let mut counter = std::collections::HashMap::<u8, i32>::new();
        for &c in s.as_bytes() {
            counter.entry(c).and_modify(|e| *e += 1).or_insert(1);
        }
        let mut seen = std::collections::HashSet::<i32>::new();
        let mut result = 0;
        for &f in counter.values() {
            let mut f = f;
            while f > 0 && seen.contains(&f) {
                f -= 1;
                result += 1;
            }
            seen.insert(f);
        }
        return result
    }
}

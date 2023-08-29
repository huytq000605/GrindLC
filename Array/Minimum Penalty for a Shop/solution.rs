impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let customers = customers.as_bytes();
        let mut come_to_late = 0;
        let mut penalty = 0;
        for &c in customers.iter() {
            if c == 'Y' as u8 {
                come_to_late += 1;
            }
        }

        let mut min_penalty = come_to_late;
        let mut result = 0;
        for (i, &c) in customers.iter().enumerate() {
            if c == 'Y' as u8 {
                come_to_late -= 1;
            } else {
                penalty += 1;
            }
            if penalty + come_to_late < min_penalty {
                min_penalty = penalty + come_to_late;
                result = i as i32 + 1;
            }
        }

        return result
    }
}

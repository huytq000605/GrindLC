impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false
        }
        let mut set = std::collections::HashSet::new();
        let mut diff = vec![];
        let mut same = false;
        let s = s.as_bytes();
        let goal = goal.as_bytes();
        for i in 0..s.len() {
            if s[i] != goal[i] {
                diff.push((s[i], goal[i]));
            }
            if set.contains(&s[i]) {
                same = true;
            }
            set.insert(s[i]);
        }
        if diff.len() == 0 && same {
            return true
        }
        if diff.len() != 2 || diff[0].0 != diff[1].1 || diff[0].1 != diff[1].0 {
            return false
        }
        return true
    }
}

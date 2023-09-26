impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        use std::collections::*;
        let mut counter = HashMap::<u8, i32>::new();
        for &c in s.as_bytes() {
            counter.entry(c).and_modify(|e| {*e += 1}).or_insert(1);
        }
        let mut visited = HashSet::new();
        let mut stack = vec![];
        for &c in s.as_bytes() {
            counter.entry(c).and_modify(|e| {*e -= 1});
            if visited.contains(&c) {
                continue
            }
            
            while stack.len() > 0 &&
                c < stack[stack.len() - 1] &&
                *counter.get(&stack[stack.len() - 1]).unwrap() > 0 {
                visited.remove(&stack.pop().unwrap());
            }
            stack.push(c);
            visited.insert(c);
        }
        return std::str::from_utf8(&stack).unwrap().to_string()
    }
}

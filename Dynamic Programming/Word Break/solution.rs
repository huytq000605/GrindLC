use std::collections::{HashSet, HashMap};

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let s = s.as_bytes();
        let mut words = HashSet::new();
        for word in word_dict {
            words.insert(word);
        }
        let mut memo = HashMap::new();
        fn dfs(s: &[u8], words: &HashSet<String>, i: usize, memo: &mut HashMap<usize, bool>) -> bool {
            if i >= s.len() {
                return true
            }
            match memo.get(&i) {
                Some(r) => return *r,
                None => {}
            };
            for j in i..s.len() {
                let ss = String::from_utf8(s[i..j+1].to_vec()).unwrap();
                if words.contains(&ss) && dfs(s, words, j+1, memo) {
                    return true
                }
            }
            memo.insert(i, false);
            return false
        }
        return dfs(&s, &words, 0, &mut memo)
    }
}

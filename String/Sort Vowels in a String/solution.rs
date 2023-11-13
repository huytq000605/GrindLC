impl Solution {
    pub fn sort_vowels(s: String) -> String {
        let vowels = vec!['u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I'];
        let mut vowel_idxs = vec![];
        let mut vowel_chrs = vec![];
        for (i, c) in s.chars().enumerate() {
            if vowels.contains(&c) {
                vowel_idxs.push(i);
                vowel_chrs.push(c);
            }
        }
        vowel_chrs.sort();

        let mut result = vec![];
        let mut j = 0;
        for (i, c) in s.chars().enumerate() {
            if j < vowel_idxs.len() && vowel_idxs[j] == i {
                result.push(vowel_chrs[j]);
                j += 1;
            } else {
                result.push(c);
            }
        }

        return result.iter().collect()
    }
}

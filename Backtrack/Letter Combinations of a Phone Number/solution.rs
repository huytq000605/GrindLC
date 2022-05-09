use std::collections::HashMap;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.len() == 0 {
            return vec![]
        };
        
        let letters: HashMap::<char, Vec<char>> = vec![
            ('2', vec!['a', 'b', 'c']),
            ('3', vec!['d', 'e', 'f']),
            ('4', vec!['g', 'h', 'i']),
            ('5', vec!['j', 'k', 'l']),
            ('6', vec!['m', 'n', 'o']),
            ('7', vec!['p', 'q', 'r', 's']),
            ('8', vec!['t', 'u', 'v']),
            ('9', vec!['w', 'x', 'y', 'z'])
        ].into_iter().collect();
        
        let mut current_level: Vec<String> = vec!["".to_string()];
        
        for digit in digits.chars() {
            let mut next_level = vec![];
            for current in current_level.iter() {
                for c in letters.get(&digit).unwrap() {
                    next_level.push(format!("{}{}", current, c));
                }
            }
            current_level = next_level;
        }
        return current_level
    }
}
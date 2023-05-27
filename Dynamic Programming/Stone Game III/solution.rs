impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        use std::collections::HashMap;
        let mut memo: HashMap<usize, i32> = HashMap::new();
        fn dfs(idx : usize, piles: &Vec<i32>, memo: &mut HashMap<usize, i32>) -> i32 {
            if idx >= piles.len() {
                return 0
            }
            if memo.contains_key(&idx) {
                return *memo.get(&idx).unwrap()
            }
            let mut s = 0;
            let mut result = std::i32::MIN;
            for i in idx..std::cmp::min(piles.len(), idx + 3) {
                s += piles[i];
                result = std::cmp::max(result, s - dfs(i + 1, piles, memo));
            }
            memo.insert(idx, result);
            return result
        }
        let diff = dfs(0, &stone_value, &mut memo);
        if diff > 0 {
            "Alice".to_string()
        } else if diff < 0 {
            "Bob".to_string()
        } else {
            "Tie".to_string()
        }
    }
}

impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        fn dfs(i: usize, m: i32, piles: &Vec<i32>, memo: &mut std::collections::HashMap<(usize, i32),i32>) -> i32 {
            if i >= piles.len() {
                return 0
            }
            if memo.contains_key(&(i, m)) {
                return *memo.get(&(i, m)).unwrap();
            }
            let mut result = std::i32::MIN;
            let mut s = 0;
            for j in i..std::cmp::min(piles.len(), i + (m*2) as usize) {
                s += piles[j];
                result = std::cmp::max(result, s - dfs(j+1, std::cmp::max(m, (j-i+1) as i32), piles, memo));
            }
            memo.insert((i, m), result);
            return result
        }
        let sub = dfs(0, 1, &piles, &mut std::collections::HashMap::new());
        let sum: i32 = piles.iter().sum();
        return (sum + sub) / 2
    }
}

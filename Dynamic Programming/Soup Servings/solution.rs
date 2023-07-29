use std::collections::HashMap;
impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        if n > 4800 {
            return 1.0
        }
        let mut memo = HashMap::new();
        fn dfs(a: i32, b: i32, memo: &mut HashMap<(i32, i32), f64>) -> f64 {
            if a <= 0 && b <= 0 {
                return 0.5
            }
            if a <= 0 {
                return 1.0
            }
            if b <= 0 {
                return 0.0
            }
            
            if memo.contains_key(&(a, b)) {
                return *memo.get(&(a, b)).unwrap()
            }
            let result = 0.25 * (dfs(a-100, b, memo) + dfs(a-75, b-25, memo) + dfs(a-50, b-50, memo) + dfs(a-25, b-75, memo));
            memo.insert((a, b), result);
            return result
        }
        return dfs(n, n, &mut memo)
    }
}

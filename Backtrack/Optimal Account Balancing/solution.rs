impl Solution {
    pub fn min_transfers(transactions: Vec<Vec<i32>>) -> i32 {
        let mut states: Vec<i32> = vec![0; 12];
        for tr in transactions {
            let (u, v, a) = match &tr[..] {
                [u, v, a] => (*u, *v, *a),
                _ => panic!("unexpected")
            };
            states[u as usize] -= a;
            states[v as usize] += a;
        }
        let mut states: Vec<i32> = states.into_iter().filter(|s| *s != 0).collect();
        fn dfs(states: &mut Vec<i32>, i: usize) -> i32 {
            if i >= states.len() {
                return 0
            }
            if states[i] == 0 {
                return dfs(states, i + 1)
            }
            let mut result = 12;
            for j in i+1..states.len() {
                if states[i] * states[j] < 0 {
                    states[j] += states[i];
                    result = std::cmp::min(result, 1+dfs(states, i+1));
                    states[j] -= states[i];
                }
            }
            return result
        }
        return dfs(&mut states, 0)
    }
}

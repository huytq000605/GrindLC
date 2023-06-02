impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let n = bombs.len();
        let mut seen = vec![0; n];
        let mut result = 0;

        fn dfs(i: i32, seen: &mut Vec<i32>, bombs: &Vec<Vec<i32>>) -> i32 {
            seen[i as usize] = 1;
            let mut result = 1;
            let (x1, y1, r1): (i64, i64, i64) = match bombs[i as usize][..] {
                [x1, y1, r1] => (x1 as i64, y1 as i64, r1 as i64),
                _ => (0, 0, 0)
            };
            for j in 0..bombs.len() {
                if seen[j] == 1 {
                    continue
                }
                let (x2, y2): (i64, i64) = match bombs[j as usize][..] {
                    [x1, y1, _] => (x1 as i64, y1 as i64),
                    _ => (0, 0)
                };
                if (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 * r1) as i64 {
                    result += dfs(j as i32, seen, bombs);
                }
            }
            return result
        }

        for i in 0..n {
            result = std::cmp::max(result, dfs(i as i32, &mut seen, &bombs));
            seen = seen.iter().map(|e| 0).collect();
        }
        return result
    }
}

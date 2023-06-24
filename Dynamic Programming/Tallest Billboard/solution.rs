impl Solution {
    pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
        const OFFSET: usize = 5000;
        let mut dp = vec![vec![-2; 10000]; rods.len()];
        fn dfs(rods: &Vec<i32>, i: i32, diff: i32, dp: &mut Vec<Vec<i32>>) -> i32 {
            if i >= rods.len() as i32 {
                if diff == 0 {
                    return 0
                }
                return -1
            }
            if dp[i as usize][diff as usize + OFFSET] != -2 {
                return dp[i as usize][diff as usize + OFFSET]
            }
            let mut a = 0;
            if dfs(rods, i+1, diff + rods[i as usize], dp) != -1 {
                a = rods[i as usize] + dfs(rods, i+1, diff + rods[i as usize], dp);;;;
            } else {
                a = -1;
            }
            let b = dfs(rods, i+1, diff - rods[i as usize], dp);
            let c = dfs(rods, i+1, diff, dp);
            dp[i as usize][diff as usize + OFFSET] = *vec![a, b, c].iter().max().unwrap();
            return dp[i as usize][diff as usize + OFFSET];
        }
        return dfs(&rods, 0, 0, &mut dp)
    }
}

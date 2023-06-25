impl Solution {
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut dp = vec![vec![-1; fuel as usize + 1]; locations.len()];

        fn dfs(locations: &Vec<i32>, cur: i32, finish: i32, fuel: i32, dp: &mut Vec<Vec<i32>>) -> i32 {
            if fuel < 0 { return 0 }
            if dp[cur as usize][fuel as usize] != -1 {
                return dp[cur as usize][fuel as usize]
            }
            let mut result = 0;
            if cur == finish { result += 1; }
            for next in 0..locations.len() as i32 {
                if next == cur { continue }
                let diff = (locations[cur as usize] - locations[next as usize]).abs();
                result = (result + dfs(locations, next, finish, fuel - diff, dp)) % MOD;
            }
            dp[cur as usize][fuel as usize] = result;
            return result
        }

        return dfs(&locations, start, finish, fuel, &mut dp)
    }
}

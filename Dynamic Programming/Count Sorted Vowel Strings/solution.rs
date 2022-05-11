impl Solution {
	pub fn count_vowel_strings(n: i32) -> i32 {
			let n = n as usize;
			let mut dp:Vec<Vec<i32>> = vec![vec![0; 6]; n + 1];
			for i in 1..6 {
					dp[1][i] = 1;
			}
			
			for i in 2..n+1 {
					for j in 1..6 {
							for k in 1..j+1 {
									dp[i][j] += dp[i-1][k];
							}
					}
			}
			let mut result = 0;
			for i in 1..6 {
					result += dp[n][i];
			}
			return result
	}
}
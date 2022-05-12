impl Solution {
	pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
			let mut result: Vec<Vec<i32>> = vec![];
			let mut cur: Vec<i32> = vec![];
			
			fn dfs(num: i32, sum: i32, cur: &mut Vec<i32>, result: &mut Vec<Vec<i32>>, k:i32, n:i32) {
					let len = cur.len() as i32;
					if len == k && sum == n {
							result.push(cur.clone());
					}
					if sum >= n || num > 9 || len >= k {
							return
					}
					cur.push(num);
					dfs(num + 1, sum + num, cur, result, k, n);
					cur.pop();
					dfs(num + 1, sum, cur, result, k, n);
			}
			
			dfs(1, 0, &mut cur, &mut result, k, n);
			return result
	}
}
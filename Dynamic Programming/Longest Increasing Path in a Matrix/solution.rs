impl Solution {
	pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
			let (m, n) = (matrix.len(), matrix[0].len());
			let mut levels = vec![vec![0; n]; m];
			let dirs = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];
			
			fn dfs(r: usize, c: usize, levels: &mut Vec<Vec<i32>>, dirs: &Vec<(i32, i32)>, matrix: &Vec<Vec<i32>>, m: usize, n: usize) -> i32 {
					if levels[r][c] != 0 {
							return levels[r][c]
					}
					let mut result = 0;
					for (dr, dc) in dirs {
							let (nr, nc) = (r as i32 + dr, c as i32 + dc);
							if nr < 0 || nc < 0 || nr >= m as i32 || nc >= n as i32 || matrix[nr as usize][nc as usize] <= matrix[r][c] {
									continue;
							}
							result = std::cmp::max(result, dfs(nr as usize, nc as usize, levels, dirs, matrix, m, n));
					}
					levels[r][c] = 1 + result;
					return 1 + result
			}
			
			let mut result = 0;
			for i in 0..m {
					for j in 0..n {
							result = std::cmp::max(result, dfs(i, j, &mut levels, &dirs, &matrix, m, n));
					}
			}
			return result
	}
}
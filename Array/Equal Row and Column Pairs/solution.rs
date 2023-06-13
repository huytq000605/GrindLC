impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut result = 0;
        for r in 0..n {
            for c in 0..n {
                let mut eq = true;
                for i in 0..n {
                    if grid[r][i] != grid[i][c] {
                        eq = false;
                        break
                    }
                }
                if eq {
                    result += 1;
                }
            }
        }
        return result
    }
}

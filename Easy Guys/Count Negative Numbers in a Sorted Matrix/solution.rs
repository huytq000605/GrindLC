impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut c: i32 = n as i32 - 1;
        let mut result = 0;
        for r in 0..m {
            while c >= 0 && grid[r][c as usize] < 0 {
                c -= 1;
            }
            result += n as i32 -c-1;
        }
        return result as i32
    }
}

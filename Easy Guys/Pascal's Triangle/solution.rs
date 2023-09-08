impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![vec![1]];
        for i in 2..num_rows as usize + 1 {
            let last_row = &result[result.len() - 1];
            let mut row = vec![1 as i32; i];
            for col in 1..i-1 {
                row[col] = last_row[col-1] + last_row[col];
            }
            result.push(row);
        }
        return result
    }
}

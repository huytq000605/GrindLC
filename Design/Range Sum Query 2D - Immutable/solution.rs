struct NumMatrix {
    prefix: Vec<Vec<i32>>
}
/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumMatrix {

    fn new(matrix: Vec<Vec<i32>>) -> Self {
        let (m, n) = (matrix.len(), matrix[0].len());
        let mut prefix = vec![vec![0; n + 1]; m + 1];
        for i in (0..m) {
            for j in (0..n) {
                prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j];
                prefix[i+1][j+1] += matrix[i][j];
            }
        }
        return NumMatrix {
            prefix: prefix
        }
    }
    
    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        let (row1, col1, row2, col2) = (row1 as usize, col1 as usize, row2 as usize, col2 as usize);
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj = NumMatrix::new(matrix);
 * let ret_1: i32 = obj.sum_region(row1, col1, row2, col2);
 */

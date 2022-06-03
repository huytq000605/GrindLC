package main

type NumMatrix struct {
    matrix [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    m, n := len(matrix), len(matrix[0])
    prefix_matrix := make([][]int, m + 1)
    prefix_matrix[0] = make([]int, n + 1)
    for i := 0; i < m; i++ {
        prefix_matrix[i+1] = make([]int, n + 1)
        for j := 0; j < n; j++ {
            prefix_matrix[i+1][j+1] = prefix_matrix[i][j+1] + prefix_matrix[i+1][j] - prefix_matrix[i][j]
            prefix_matrix[i+1][j+1] += matrix[i][j]
        }
    }
    return NumMatrix {
        matrix: prefix_matrix,
    }
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.matrix[row2+1][col2+1] + this.matrix[row1][col1] - this.matrix[row2+1][col1] - this.matrix[row1][col2+1]
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */

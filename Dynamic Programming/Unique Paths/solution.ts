function uniquePaths(m: number, n: number): number {
    let result = Array(m).fill([]).map(e => Array(n).fill(0))
    for(let i = 0; i < result[0].length; i++) {
        result[0][i] = 1
    }
    for(let i = 0; i < result.length; i++) {
        result[i][0] = 1
    }
    for(let i = 1; i < result.length; i++) {
        for(let j = 1; j < result[0].length; j++) {
            result[i][j] = result[i-1][j] + result[i][j-1]
        }
    }
    return result[m-1][n-1]
};
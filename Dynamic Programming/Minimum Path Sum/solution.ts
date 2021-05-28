/*
Create an array (m+1)*(n+1), because we can only move to the left or right, then row = 1 and col = 1 can only go from [1, 1]
Then all the rest is following by min(top, left) + value(cell)
*/

function minPathSum(grid: number[][]): number {
    let result = Array(grid.length + 1).fill([]).map(() => Array(grid[0].length + 1).fill(0))
    for(let i = 1; i < result.length; i++) {
        for(let j = 1; j < result[0].length; j++) {
            if(i == 1) {
                result[i][j] = result[i][j-1] + grid[i-1][j-1]
                continue;
            }
            if(j == 1) {
                result[i][j] = result[i-1][j] + grid[i-1][j-1]
                continue;
            }
            result[i][j] = Math.min(result[i-1][j], result[i][j-1]) + grid[i-1][j-1]
        }
        
    }
    return result[grid.length][grid[0].length]
};
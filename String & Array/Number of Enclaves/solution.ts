/*
Mutate all 1 to 0 if it connected to boundary then count all the rest 1
*/

function numEnclaves(grid: number[][]): number {
    let result = 0
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(i == 0 || i == grid.length - 1 || j == 0 || j == grid[0].length - 1) 
                helper(grid, i, j)
        }
    }
    for(let i = 1; i < grid.length - 1; i++) {
        for(let j = 1; j < grid[0].length - 1; j++) {
            if(grid[i][j]) result++
        }
    }
    return result
};

function helper(grid, i, j) {
    if(i < 0 || i == grid.length || j < 0 || j == grid[0].length || grid[i][j] == 0) return;
        grid[i][j] = 0
        helper(grid, i, j + 1)
        helper(grid, i, j - 1)
        helper(grid, i + 1, j)
        helper(grid, i - 1, j)
}
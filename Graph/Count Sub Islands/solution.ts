/*
So first we remove all (mutating grid2) the island which are not appear in grid1 , then just count island in grid2
*/
function countSubIslands(grid1: number[][], grid2: number[][]): number {
    let m = grid1.length;
    let n = grid1[0].length
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid1[i][j] === 0 && grid2[i][j] === 1) {
                dfs(grid2, i, j)
            }
        }
    }
    let result = 0
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid2[i][j] === 1) {
                dfs(grid2, i, j)
                result++
            }
        }
    }
    return result
};

function dfs(grid2: number[][], i: number, j:number) {
    if(i < 0 || i === grid2.length || j < 0 || j === grid2[0].length || grid2[i][j] === 0) {
        return
    }
    
    grid2[i][j] = 0
    
    dfs(grid2, i + 1, j)
    dfs(grid2, i - 1, j)
    dfs(grid2, i, j + 1)
    dfs(grid2, i, j - 1)
}
    
function swimInWater(grid: number[][]): number {
    let min = 0
    let max = 50 * 50
    while(min < max) {
        let mid = min + Math.floor((max - min)/ 2)
        let seen = new Array(grid.length).fill(0).map(each => Array(grid.length).fill(-1))
        if(!dfs(grid, 0, 0, mid, seen)) {
            min = mid + 1
        } else {
            max = mid
        }
    }
    return min
};

function dfs(grid: number[][], i: number, j: number, limit: number, seen: number[][]) {
    if(i < 0 || i === grid.length || j < 0 || j === grid.length || grid[i][j] > limit) {
        return false
    }
    if(i === grid.length - 1 && j === grid.length - 1) {
        return true
    }
    if(seen[i][j] !== -1) {
        return false
    }
    seen[i][j] = 1
    const dirs = [[1,0], [0,1], [-1, 0], [0, -1]]
    for(let dir of dirs) {
        if(dfs(grid, i + dir[0], j + dir[1], limit, seen))
            return true
    }
    return false
}
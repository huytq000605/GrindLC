// We use binary search to find limit
// We use dfs to see if we can traverse to the final node
// Dont need to store seen map for each path 

function minimumEffortPath(grid: number[][]): number {
    let min = 0
    let max = 1000000;
    while(min < max) {
        let mid = min + Math.floor((max - min)/2)
        let seen = new Set<string>()
        if(!dfs(grid, 0, 0, mid, grid[0][0], seen)) {
            min = mid + 1
        } else {
            max = mid
        }
    }
    return min
};

function dfs(grid: number[][], i: number, j: number, limit: number, prev: number, seen: Set<string>) {
    if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || Math.abs(grid[i][j] - prev) > limit) {
        return false
    }
    if(i === grid.length - 1 && j === grid[0].length - 1) {
        return true
    }
    const key = `${i}-${j}`
    
    if(seen.has(key)) {
        return false
    }
    seen.add(key)
    
    let directions = [[0,1], [1,0], [-1,0], [0, -1]]
    for(let dir of directions) {
        if(dfs(grid, i + dir[0], j + dir[1], limit, grid[i][j], seen) === true) {
            return true
        }
    }
    return false
    
}
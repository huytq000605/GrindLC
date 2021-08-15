function latestDayToCross(row: number, col: number, cells: number[][]): number {
    let dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
    let dfs = (i , j, seen, grid) => {
        if(i === row - 1) return true
        if(seen[i][j] !== 0) return false
        seen[i][j] = 1
        for(let dir of dirs) {
            let x = i + dir[0]
            let y = j + dir[1]
            if(x < 0 || x >= row || y < 0 || y >= col || grid[x][y] === 1 || (seen[x][y] !== 0)) continue
            if(dfs(x, y, seen, grid)) return true
        }
        return false
    }
    
    let min = 0
    let max = cells.length
    while(min < max) {
        let mid = min + Math.floor((max - min + 1)/2)
        let grid = Array(row).fill(0).map(() => Array(col).fill(0))
        let result = false
        for(let [idx, cell] of cells.entries()) {
            if(idx >= mid) break
            grid[cell[0] - 1][cell[1] - 1] = 1
        }
        let seen = Array(row).fill(0).map(() => Array(col).fill(0))
        for(let start = 0; start < col; start++) {
            if(grid[0][start] === 0 && seen[0][start] === 0) {
                if(dfs(0, start, seen, grid) === true) {
                    result = true
                    break
                }
            }
            
        }
        if(result === true) {
            min = mid
        } else {
            max = mid - 1
        }
    }
    
    return min
};
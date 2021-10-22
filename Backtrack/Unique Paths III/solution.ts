function uniquePathsIII(grid: number[][]): number {
    let seen = new Set()
    const dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    let result = 0
    let obstacles = 0
    let startPoint = [0, 0]
    
    let getId = (row, col) => {
        return row * grid[0].length + col
    }
    
    let dfs = (i, j) => {
        if(grid[i][j] === 2) {
            if(seen.size + 1 + obstacles === grid.length * grid[0].length) result++
            return
        }
        for(let dir of dirs) {
            let nr = i + dir[0]
            let nc = j + dir[1]
            let id = getId(nr, nc)
            if(nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || grid[nr][nc] === 1 || grid[nr][nc] === -1 || seen.has(id)) continue
            
            seen.add(id)
            dfs(nr, nc)
            seen.delete(id)
        }
    }
    
    
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === 1) {
                startPoint = [i ,j]
            }
            if(grid[i][j] === -1) obstacles++
        }
    }
    
    dfs(startPoint[0], startPoint[1])
    
    return result
    
};
function orangesRotting(grid: number[][]): number {
    let fresh = 0
    let queue = []
    const dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === 2) {
                queue.push([i, j, 0])
            }
            if(grid[i][j] === 1) {
                fresh++
            }
        }
    }
    if(fresh === 0) return 0
    
    while(queue.length > 0) {
        let [i, j, depth] = queue.shift()
        if(grid[i][j] === 1) {
            fresh--
            if(fresh === 0) {
                return depth
            }
            grid[i][j] = 2 
        }
        for(let dir of dirs) {
            let r = i + dir[0]
            let c = j + dir[1]
            if(r < 0 || r === grid.length || c < 0 || c === grid[0].length || grid[r][c] !== 1) {
                continue
            }
            queue.push([r, c, depth + 1])
        }
    }
    
    return -1
};

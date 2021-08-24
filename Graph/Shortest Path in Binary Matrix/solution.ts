function shortestPathBinaryMatrix(grid: number[][]): number {
    if(grid[0][0] === 1) return -1
    let dirs = [[0,1], [1,0], [1,1], [-1, -1], [-1, 0], [0, -1], [-1, 1], [1, -1]]
    let queue = [[0,0,1]]
    let seen = Array(grid.length).fill(0).map(() => Array(grid.length))
    seen[0][0] = true
    while(queue.length) {
        let [i, j, dist] = queue.shift()
        if(i === grid.length - 1 && j === grid.length - 1) return dist
        for(let dir of dirs) {
            let x = i + dir[0]
            let y = j + dir[1]
            if(x < 0 || x >= grid.length || y < 0 || y >= grid.length || seen[x][y] !== undefined || grid[x][y] === 1) continue
            seen[x][y] = true
            queue.push([x, y, dist + 1])
        }
    }
    return -1
};
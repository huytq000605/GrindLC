function shortestPath(grid: number[][], k: number): number {
    let dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    let queue = []
    let cache = Array(grid.length).fill(0).map(() => Array(grid[0].length)) // Visited
    queue.push([0, 0, k, 0])
    while(queue.length) {
        let [i, j, k, step] = queue.shift()
        if(i === grid.length - 1 && j === grid[0].length - 1) return step
        for(let dir of dirs) {
            let row = i + dir[0]
            let col = j + dir[1]
            if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || (grid[row][col] === 1 && k === 0)) continue
            if(cache[row][col] !== undefined) { // If visited this before, compare step and k to pass
                let [oldK, oldStep] = cache[row][col]
                if(grid[row][col] === 1) {
                    if(oldK >= k - 1 && oldStep <= step + 1) continue
                } else {
                    if(oldK >= k && oldStep <= step + 1) continue
                }
            }
            if(grid[row][col] === 1) {
                cache[row][col] = [k - 1, step + 1]
                queue.push([row, col, k - 1, step + 1])
            } else {
                cache[row][col] = [k, step + 1]
                queue.push([row, col, k, step + 1])
            }
        }
    }
    return -1
};
function shortestBridge(grid: number[][]): number {
    let seen = new Map()
    let queue = []

	// Get all cells of first island for seen and queue (Union Find)
    outer:
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === 1) {
                dfs(grid, i, j, seen, queue)
                break outer
            }
        }
    }

    const directions = [[0,1], [1,0], [-1, 0], [0, -1]]
    while(queue.length > 0) { // Breath-first search
        let [i, j, distance] = queue.shift()
        const key = `${i}-${j}`
        if(seen.has(key) && distance !== 0) { // Initial go from first island
            continue
        }
        if(!seen.has(key) && grid[i][j] === 1) { // We meet second island
            return distance - 1
        }
        seen.set(key, true)
        for(let direction of directions) {
            let newRow = i + direction[0]
            let newCol = j + direction[1]
            if(!seen.has(`${newRow}-${newCol}`) && newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol <= grid[0].length)
                queue.push([i + direction[0], j + direction[1], distance + 1])
        }
    }
    return 0 // Never reach here
};

function dfs(grid: number[][], i: number, j: number, seen: Map<string, boolean>, queue: Array<[number, number, number]>) {
    if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] === 0) {
        return -1
    }
    const key = `${i}-${j}`
    if(seen.has(key)) {
        return 0
    }
    seen.set(key, true)
    const directions = [[0,1], [1,0], [-1, 0], [0, -1]]
    for(let direction of directions) {
        dfs(grid, i + direction[0], j + direction[1], seen, queue)
    }
    queue.push([i, j, 0])
}

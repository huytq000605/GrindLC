function maxDistance(grid: number[][]): number {
    let n = grid.length
    let queue = []
    let distance = Array(n).fill(0).map(() => Array(n)) // Smallest distance from this [i][j] to Island
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(grid[i][j] === 1) {
                distance[i][j] = 0
                queue.push([i, j, 0])
            } else {
                distance[i][j] = Number.MAX_SAFE_INTEGER
            }
        }
    }
    
    if(queue.length === 0 || queue.length === n*n) return -1 // If all is island or all is water
    
	let dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]
    
    while(queue.length > 0) {
		let [i, j, currentDistance] = queue.shift()
        for(let dir of dirs) {
			let x = i + dir[0]
            let y = j + dir[1]
            if(x < 0 || x >= n || y < 0 || y >= n) continue
            if(currentDistance + 1 < distance[x][y]) { // If this distance can be lower
				distance[x][y] = currentDistance + 1
                queue.push([x,y, currentDistance + 1])
            }
        }
    }
    
	let result = Number.MIN_SAFE_INTEGER
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            result = Math.max(result, distance[i][j])
        }
    }
    return result
    
};
function orangesRotting(grid: number[][]): number {
    let deque = []
    let deque1 = []
    let totalFresh = 0
    let result = 0
    
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[0].length; j++) {
            if(grid[i][j] === 1) totalFresh++
            if(grid[i][j] === 2) deque.push([i, j])
        }
    }
    
    const dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
    while(deque.length) {
        let [i, j] = deque.shift()
        for(let dir of dirs) {
            let newRow = i + dir[0]
            let newCol = j + dir[1]
            if(newRow < 0 || newRow >= grid.length || newCol < 0 || newCol >= grid[0].length || grid[newRow][newCol] !== 1) continue
            totalFresh--
            grid[newRow][newCol] = 2
            deque1.push([newRow, newCol])
        }
        if(!deque.length) {
            if(!deque1.length) break
            result++
            [deque, deque1] = [deque1, deque]
        }
        
    }
    
    if(totalFresh !== 0) return -1
    return result
};
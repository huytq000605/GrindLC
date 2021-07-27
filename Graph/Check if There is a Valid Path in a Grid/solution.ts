function hasValidPath(grid: number[][]): boolean {
    let map = new Map()
    map.set(1, [[0, 1], [0, - 1]])
    map.set(2, [[-1, 0], [1, 0]])
    map.set(3, [[1, 0], [0, -1]])
    map.set(4, [[0, 1], [1, 0]])
    map.set(5, [[-1, 0], [0, -1]])
    map.set(6, [[-1 ,0], [0, 1]])
    let seen = new Set()
    function dfs(current: [number, number], prev: [number, number]) {
        if(!(current[0] === 0 && current[1] === 0)) {
            let haveDir = false
            for(let dir of map.get(grid[current[0]][current[1]])) {
                let prevRow = current[0] + dir[0]
                let prevCol = current[1] + dir[1]
                if(prevRow < 0 || prevRow >= grid.length || prevCol < 0 || prevCol >= grid[0].length) continue
                if(prevRow === prev[0] && prevCol === prev[1]) {
                    haveDir = true
                }
                
            }
            if(!haveDir) return false
        }
        if(current[0] === grid.length - 1 && current[1] === grid[0].length - 1) return true
        seen.add(`${current[0]},${current[1]}`)
        for(let dir of map.get(grid[current[0]][current[1]])) {
            let newRow = current[0] + dir[0]
            let newCol = current[1] + dir[1]
            if(newRow < 0 || newRow >= grid.length || newCol < 0 || newCol >= grid[0].length || seen.has(`${newRow},${newCol}`)) continue
            if(dfs([newRow, newCol], current)) return true
        }
        return false
    }
    return dfs([0, 0], [-1, -1]) 
};
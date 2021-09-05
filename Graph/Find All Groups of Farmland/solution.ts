function findFarmland(land: number[][]): number[][] {
    let seen = Array(land.length).fill(0).map(() => Array(land[0].length))
    let count = 0
    let dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    let bottom = Number.MIN_SAFE_INTEGER
    let right = Number.MIN_SAFE_INTEGER
    
    let dfs = (i, j) => {
        seen[i][j] = 1
        bottom = Math.max(i, bottom)
        right = Math.max(right, j)
        count++
        for(let dir of dirs) {
            let newRow = i + dir[0]
            let newCol = j + dir[1]
            if(newRow < 0 || newRow >= land.length || newCol < 0 || newCol >= land[0].length || seen[newRow][newCol] || land[newRow][newCol] === 0) continue
            dfs(newRow, newCol)
        }
    }
    
    let result = []
    
    for(let i = 0; i < land.length; i++) {
        for(let j = 0; j < land[0].length; j++) {
            if(land[i][j] === 1 && !seen[i][j]) {
                dfs(i, j)
                let edge1 = bottom - i + 1
                let edge2 = right - j + 1
                if(edge1 * edge2 === count) {
                    result.push([i, j, bottom, right])
                }
                bottom = Number.MIN_SAFE_INTEGER
                right = Number.MIN_SAFE_INTEGER
                count = 0
            }
        }
    }
    
    return result
};
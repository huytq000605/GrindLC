function updateMatrix(mat: number[][]): number[][] {
    let result = Array(mat.length).fill(0).map(() => Array(mat[0].length).fill(Number.MAX_SAFE_INTEGER))
    let dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
    let queue = []
    
    function bfs() {
        while(queue.length > 0) {
            let [row, col, currentDist] = queue.shift()
            result[row][col] = Math.min(result[row][col], currentDist)
            for(let dir of dirs) {
                let newRow = row + dir[0]
                let newCol = col + dir[1]
                if(newRow < 0 || newRow >= mat.length || newCol < 0 || newCol >= mat[0].length || mat[newRow][newCol] === 0 || result[newRow][newCol] <= currentDist + 1) continue
                queue.push([newRow, newCol, currentDist + 1])
            }
        }
    }
    
    
    for(let i = 0 ; i < mat.length; i++) {
        for(let j = 0; j < mat[0].length; j++) {
            if(mat[i][j] === 0) {
                result[i][j] = 0
                queue.push([i, j, 0])
            }
        }
    }
    
    bfs()
    
    return result
};
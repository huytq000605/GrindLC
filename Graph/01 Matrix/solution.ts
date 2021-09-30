function updateMatrix(mat: number[][]): number[][] {
    let result = Array(mat.length).fill(0).map(() => Array(mat[0].length).fill(Number.MAX_SAFE_INTEGER))
    let queue = []
    for(let row = 0; row < mat.length; row++) {
        for(let col = 0; col < mat[0].length; col++) {
            if(mat[row][col] === 0) {
                result[row][col] = 0
                queue.push([row, col, 0])
            }
        }
    }
    
    let dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
    
    while(queue.length) {
        let [row, col, distance] = queue.shift()
        for(let dir of dirs) {
            let newRow = row + dir[0]
            let newCol = col + dir[1]
            if(newRow < 0 || newRow >= mat.length || newCol < 0 || newCol >= mat[0].length || distance + 1 >= result[newRow][newCol]) continue
            result[newRow][newCol] = distance + 1
            queue.push([newRow, newCol, distance + 1])
        }
    }
    
    return result
    
};
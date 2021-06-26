function findDiagonalOrder(mat: number[][]): number[] {
    let diagonalMap = new Map()
    for(let i = 0; i < mat.length; i++) {
        for(let j = 0; j < mat[0].length; j++) {
            if(!diagonalMap.has(i+j)) diagonalMap.set(i+j, [])
            if((i + j) % 2 === 0) {
                diagonalMap.get(i+j).unshift(mat[i][j])
            } else {
                diagonalMap.get(i+j).push(mat[i][j])
            }
        }
    }
    let result = []
    for(let diagonal of diagonalMap.values()) {
        result.push(...diagonal)
    }
    return result
};
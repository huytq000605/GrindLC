function construct2DArray(original: number[], m: number, n: number): any {
    if(m * n !== original.length) return []
    let result = Array(m).fill(0).map(() => Array(n))
    for(let i = 0; i < original.length; i++) {
        let row = Math.floor(i / n)
        let col = i % n
        result[row][col] = original[i]
    }
    return result
};
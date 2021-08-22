function minimizeTheDifference(mat: number[][], target: number): number {   
    let cache = Array(mat.length).fill(0).map(() => Array(mat.length * 70))
    let finalResult = Number.MAX_SAFE_INTEGER // store a global variable when dfs to break ASAP
    let dfs = (row: number, current: number) => {
        if(row === mat.length) {
            let diff = Math.abs(current - target)
            finalResult = Math.min(finalResult, diff)
            return diff
        }
        if(cache[row][current] !== undefined) return cache[row][current]
        let result = Number.MAX_SAFE_INTEGER
        for(let col = 0; col < mat[0].length; col++) {
            if(current + mat[row][col] - target >= finalResult) continue // break ASAP
            result = Math.min(result, dfs(row + 1, current + mat[row][col]))
        }
        cache[row][current] = result
        return result
    }
    
    dfs(0, 0)
    return finalResult
};
function gridGame(grid: number[][]): number {
    let prefixTop = Array(grid[0].length)
    let prefixBot = Array(grid[0].length)
    prefixTop[0] = grid[0][0]
    prefixBot[0] = grid[1][0]
    for(let i = 1; i < grid[0].length; i++) {
        prefixTop[i] = prefixTop[i-1] + grid[0][i]
        prefixBot[i] = prefixBot[i-1] + grid[1][i]
    }
    let result = Number.MAX_SAFE_INTEGER
    for(let goBottom = 0; goBottom < grid[0].length; goBottom++) {
        let res = prefixTop[grid[0].length - 1] - prefixTop[goBottom]
        if(goBottom > 0) {
            res = Math.max(res, prefixBot[goBottom - 1])
        }
        result = Math.min(result, res)
    }
    return result
};
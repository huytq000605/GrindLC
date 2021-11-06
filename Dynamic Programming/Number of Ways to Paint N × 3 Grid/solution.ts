// Time complexity: n * 3^3 * 3^3
// Space complexity: n * 2^6 + log(n)
function numOfWays(n: number): number {
    let dp = Array(n).fill(0).map(() => Array(1 << (3 * 2)))
    let colors = [1, 2, 3]
    let MOD = 1e9 + 7
    
    let dfs = (row: number, col: number, previousRow: number, currentRow: number) => {
        if(row >= n) return 1
        if(col >= 3) return dfs(row + 1, 0, currentRow, 0)
        if(col === 0 && dp[row][previousRow] !== undefined) return dp[row][previousRow]
        let result = 0
        let top = (previousRow >> (col * 2)) & 0b11
        let left = (currentRow >> ((col-1) * 2)) & 0b11
        let original = currentRow
        for(let color of colors) {
            if(color === left || color === top) continue
            currentRow |= (color << (col * 2))
            result += dfs(row, col + 1, previousRow, currentRow)
            result %= MOD
            currentRow = original
        }
        if(col === 0) dp[row][previousRow] = result
        return result
    }
    
    return dfs(0, 0, 0, 0)
};
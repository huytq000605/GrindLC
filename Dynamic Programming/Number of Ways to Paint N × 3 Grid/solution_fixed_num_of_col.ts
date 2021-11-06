// Time complexity: n * (3 * 3 * 3) * (3 * 3 * 3) = n * 27 ^ 2
// Space complexity: n * 4^3 + log(n)
function numOfWays(n: number): number {
    let dp = Array(n).fill(0).map(() => Array(4).fill(0).map(() => Array(4).fill(0).map(() => Array(4))))
    let colors = [1,2,3]
    let MOD = 1e9 + 7
    let dfs = (row: number, col1: number, col2: number, col3: number) => {
        if(row >= n) return 1
        if(dp[row][col1][col2][col3] !== undefined) return dp[row][col1][col2][col3]
        let result = 0
        for(let c1 of colors) {
            if(c1 === col1) continue
            for(let c2 of colors) {
                if(c2 === c1 || c2 === col2) continue
                for(let c3 of colors) {
                    if(c3 === c2 || c3 === col3) continue
                    result += dfs(row + 1, c1, c2, c3)
                    result = result % MOD
                }
            }
        }
        dp[row][col1][col2][col3] = result % MOD
        return result % MOD
    }
    
    return dfs(0, 0, 0, 0)
};
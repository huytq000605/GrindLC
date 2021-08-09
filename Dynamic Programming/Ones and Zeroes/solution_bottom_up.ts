function findMaxForm(strs: string[], m: number, n: number): number {
    let arr = strs.map((str) => {
        let result = [0, 0]
        for(let c of str) {
            if(c === "0") result[0]++
            else result[1]++
        }
        return result
    })
    let result = 0
    let dp: any = Array(strs.length).fill(0).map(() => Array(m+1).fill(0).map(() => Array(n + 1).fill(0)))
    
    if(arr[0][0] <= m && arr[0][1] <= n) {
        dp[0][m - arr[0][0]][n - arr[0][1]] = 1
        result = 1
    }
    
    for(let i = 1; i < strs.length; i++) {
        for(let j = 0; j <= m; j++) {
            for(let k = 0; k <= n; k++) {
                if(j + arr[i][0] <= m && k + arr[i][1] <= n) { // If can plus 1
                    dp[i][j][k] = Math.max(dp[i-1][j][k], dp[i - 1][j + arr[i][0]][k +arr[i][1]] + 1)
                    result = Math.max(result, dp[i][j][k])
                } else {
                    dp[i][j][k] = dp[i-1][j][k]
                }
                    
            }
        } 
    }

    
    return result
};


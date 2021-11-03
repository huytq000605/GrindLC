function mctFromLeafValues(arr: number[]): number {
    let dp = Array(arr.length).fill(0).map(() => Array(arr.length))
    let buildTree = (start: number, end: number) => {
        if(start === end) return 0 // Leaf node so return 0, we dont count it
        if(dp[start][end] !== undefined) return dp[start][end]
        let result = Number.MAX_SAFE_INTEGER
        for(let i = start; i < end; i++) {
            let maxLeft = Math.max(...arr.slice(start, i + 1))
            let maxRight = Math.max(...arr.slice(i + 1, end + 1))
            result = Math.min(result, buildTree(start, i) + buildTree(i + 1, end) + maxLeft * maxRight)
        }
        dp[start][end] = result
        return result
    }
    let res = buildTree(0, arr.length - 1)
    return res
};
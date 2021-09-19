function maxTaxiEarnings(n: number, rides: number[][]): number {
    let dp = Array(rides.length)
    rides.sort((a,b) => a[0] - b[0])
    let dfs = (index) => {
        if(index >= rides.length) return 0
        if(dp[index] !== undefined) return dp[index]
        let result = dfs(index + 1)
        result = Math.max(result, rides[index][1] - rides[index][0] + rides[index][2])
        let min = index + 1
        let max = rides.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            if(rides[mid][0] < rides[index][1]) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        
        let nextIndex = min
        if(nextIndex < rides.length && rides[nextIndex][0] >= rides[index][1]) result = Math.max(result, rides[index][1] - rides[index][0] + rides[index][2] + dfs(nextIndex))
        dp[index] = result
        return result
    }
    return dfs(0)
};
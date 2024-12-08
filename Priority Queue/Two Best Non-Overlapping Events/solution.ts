function maxTwoEvents(events: number[][]): number {
    let dp = Array(events.length).fill(0).map(() => Array(2))
    events.sort((a,b) => a[0] - b[0])
    let dfs = (index, attempt) => {
        if(index >= events.length || attempt >= 2) return 0
        if(dp[index][attempt] !== undefined) return dp[index][attempt]
        
        let min = index + 1
        let max = events.length
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            if(events[mid][0] > events[index][1]) {
                max = mid
            } else {
                min = mid + 1
            }
        }
        
        let attendThis = events[index][2] + dfs(min, attempt + 1)
        let passThis = dfs(index + 1, attempt)
        dp[index][attempt] = Math.max(attendThis, passThis)
        return dp[index][attempt]
    }
    return dfs(0, 0)
};

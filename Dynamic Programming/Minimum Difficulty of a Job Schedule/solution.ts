function minDifficulty(jobs: number[], d: number): number {
    let dp = Array(jobs.length).fill(0).map(() => Array(d + 1))
    let dfs = (index: number, day: number) => {
        if( (index >= jobs.length && day > 0) || (jobs.length - index < day) || (day < 0)) {
            return Number.MAX_SAFE_INTEGER
        }
        if(index >= jobs.length && day === 0) {
            return 0
        }
        if(dp[index][day] !== undefined) return dp[index][day]
        let max = 0
        let result = Number.MAX_SAFE_INTEGER
        for(let i = index; i < jobs.length; i++) {
            max = Math.max(max, jobs[i])
            result = Math.min(result, max + dfs(i + 1, day - 1))
        }
        dp[index][day] = result
        return result
    }
    let result = dfs(0, d)
    if(result >= Number.MAX_SAFE_INTEGER) return -1
    return result
};
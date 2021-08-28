function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    let job = Array(startTime.length).fill(0).map((e, i) => [startTime[i], endTime[i], profit[i]])
    let max = Math.max(...endTime)
    let dp = Array(max + 1).fill(0)
    let endAt = new Map()
    for(let i = 0; i < job.length; i++) {
        if(!endAt.has(job[i][1])) endAt.set(job[i][1], [])
        endAt.get(job[i][1]).push([job[i][0], job[i][2]])
    }
    for(let i = 0; i <= max; i++) {
        if(i > 0) {
           dp[i] = dp[i-1] 
        }
        if(endAt.has(i)) {
            for(let [start, profit] of endAt.get(i)) {
                dp[i] = Math.max(dp[i], dp[start] + profit)
            }
        }
    }
    return dp[max]
    
};
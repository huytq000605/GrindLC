function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    let endAt = new Map()
    let maxTime = 0
    for(let i = 0; i < endTime.length; i++) {
        if(!endAt.has(endTime[i])) {
            endAt.set(endTime[i], [])
        }
        endAt.get(endTime[i]).push([startTime[i], profit[i]])
        maxTime = Math.max(maxTime, endTime[i])
    }
    
    let dp = Array(maxTime + 2).fill(0)
    for(let i = 0; i <= maxTime + 1; i++) {
        if(i > 0) dp[i] = dp[i-1]
        if(endAt.has(i)) {
            for(let [start, profit] of endAt.get(i)) {
                dp[i] = Math.max(dp[i], dp[start] + profit)
            }
        }
        
    }
    return dp[dp.length - 1]
};
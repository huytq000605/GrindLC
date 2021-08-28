function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    let jobs = Array(startTime.length).fill(0).map((e, i) => [startTime[i], endTime[i], profit[i]])
    jobs.sort((a,b) => a[0] - b[0])
    let cache = Array(jobs.length)
    let dfs = (index) => {
        if(index === jobs.length) return 0
        if(cache[index] !== undefined) return cache[index]
        let result = dfs(index + 1)
        let [start, end, profit] = jobs[index]
        let nextIndex = index + 1
        while(nextIndex < jobs.length && jobs[nextIndex][0] < end) {
            nextIndex++
        }
        result = Math.max(result, profit + dfs(nextIndex))
    
        cache[index] = result
        return result
    }
    let result = dfs(0)
    return result
};
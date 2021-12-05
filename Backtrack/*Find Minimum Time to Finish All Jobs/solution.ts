function minimumTimeRequired(jobs: number[], k: number): number {
    let workers = Array(k).fill(0)
    let result = Number.MAX_SAFE_INTEGER
    let dfs = (idx) => {
        if(idx >= jobs.length) {
            result = Math.min(result, Math.max(...workers))
            return Math.max(...workers)
        }
        let seen = new Set()
        let res = Number.MAX_SAFE_INTEGER
        for(let i = 0; i < workers.length; i++) {
            if(seen.has(workers[i])) continue
            if(workers[i] + jobs[idx] < result) {
                seen.add(workers[i])
                workers[i] += jobs[idx]
                res = Math.min(result, dfs(idx + 1))
                workers[i] -= jobs[idx]
            }
            
        }
        return res
    }
    return dfs(0)
    
};
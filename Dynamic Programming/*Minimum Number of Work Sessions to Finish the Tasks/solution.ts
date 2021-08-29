function minSessions(tasks: number[], sessionTime: number): number {
    let sessions = []
    let cache = new Map()
    let dfs = (index) => {
        if(index === tasks.length) return sessions.length
        let key=`${index},${JSON.stringify([...sessions].sort((a,b) => a-b))}` // The order of sessions doesn't matter
        if(cache.has(key)) return cache.get(key)
		// Try to add current index to a new session
        sessions.push(tasks[index])
        let result = dfs(index + 1)
        sessions.pop()
		// Try to add current index to existing sessions
        for(let [idx, session] of sessions.entries()) {
            if(tasks[index] + session <= sessionTime) {
                sessions[idx] += tasks[index]
                result = Math.min(result, dfs(index + 1))
                sessions[idx] -= tasks[index]
            }
        }
        cache.set(key, result)
        return result
        
    }
    return dfs(0)
};
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    let graph = new Map()
    
    for(let pre of prerequisites) {
        if(!graph.has(pre[0])) graph.set(pre[0], [])
        graph.get(pre[0]).push(pre[1])
    }
    
    let seen = new Map()
    
    function dfs(current) {
        seen.set(current, false)
        if(!graph.has(current)) {
            seen.set(current, true)
            return true
        }
        for(let pre of graph.get(current)) {
            if(seen.has(pre)) {
                if(seen.get(pre) === false) {
                    return false
                } else {
                    continue
                }
            }
            if(!dfs(pre)) return false
        }
        seen.set(current, true)
        
        return true
    }
    
    for(let i = 0; i < numCourses; i++) {
        if(seen.has(i)) continue
        if(!dfs(i)) return false
    }
    return true
    
};
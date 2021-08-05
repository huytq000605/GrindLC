function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    let graph = new Map()
    
    for(let pre of prerequisites) {
        if(!graph.has(pre[0])) graph.set(pre[0], [])
        graph.get(pre[0]).push(pre[1])
    }
    
    let result = []
    
    let seen = new Map()
    
    let dfs = (current) => {
        if(graph.has(current)) {
            for(let pre of graph.get(current)) {
                if(seen.has(pre)) {
                    if(seen.get(pre) === false) return false
                    else continue
                }
                seen.set(pre, false)
                if(!dfs(pre)) return false 
            }
        }
        result.push(current)
        seen.set(current, true)
        return true
    }
    
    for(let i = 0; i < numCourses; i++) {
        if(seen.has(i)) continue
        seen.set(i, false)
        if(!dfs(i)) return []
    }
    return result
};
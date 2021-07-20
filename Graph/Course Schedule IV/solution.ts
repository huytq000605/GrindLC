function checkIfPrerequisite(numCourses: number, prerequisites: number[][], queries: number[][]): boolean[] {
    let graph = new Map()
    for(let [need, take] of prerequisites) {
        if(!graph.has(need)) graph.set(need, [])
        graph.get(need).push(take)
    }
    let result = []
    
    function dfs(from: number, target: number, seen: Set<number>) {
        if(from === target) return true
        if(seen.has(from)) return false
        seen.add(from)
        if(graph.has(from)) {
            for(let connected of graph.get(from)) {
                if(!seen.has(connected) && dfs(connected, target, seen)) return true
            }
        }
        
        return false
    }
    for(let query of queries) {
        let res = false
        let seen = new Set<number>()
        if(dfs(query[0], query[1], seen)) {
            res = true
        }
        result.push(res)
    }
    return result
};
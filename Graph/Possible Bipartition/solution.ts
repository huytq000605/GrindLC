function possibleBipartition(n: number, dislikes: number[][]): boolean {
    let graph = new Map()
    
    for(let [people1, people2] of dislikes) {
        if(!graph.has(people1)) graph.set(people1, [])
        if(!graph.has(people2)) graph.set(people2, [])
        
        graph.get(people1).push(people2)
        graph.get(people2).push(people1)
    }
    
    let group = new Map()
    let seen = new Set()
    
    for(let i = 1; i <= n; i++) {
        if(!seen.has(i)) {
            traversal(i)
            group.set(i, 1)
        }
    }
    
    function traversal(current: number) {
        seen.add(current)
        if(graph.has(current)) {
            for(let hate of graph.get(current)) {
                if(!seen.has(hate)) traversal(hate)
            }
        }
        
    }
    
    seen = new Set()
    
    function dfs(current: number) {
        let currentGroup = group.get(current)
        seen.add(current)
        if(graph.has(current)) {
            for(let hate of graph.get(current)) {
                if(group.get(hate) === currentGroup) {
                    return false
                } else {
                    group.set(hate, 1 - currentGroup)
                }
                if(!seen.has(hate)) {
                    if(!dfs(hate)) return false
                }
            }
        }
        return true
    }
    
    
    for(let i = 1; i <= n; i++) {
        if(!dfs(i)) return false
    }
    
    return true
};
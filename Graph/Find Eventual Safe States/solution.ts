// Find node that makes a linked list graph like

function eventualSafeNodes(graph: number[][]): number[] {
    let result = []
    let cache = new Map()
    for(let i = 0; i < graph.length; i++) {
        dfs(graph, i, new Set(), cache , result)
    }
    return result.sort((a,b) => a-b)
};

function dfs(graph: number[][], index: number, seen: Set<number>, cache: Map<number, boolean>, result: number[]): boolean {
    if(cache.has(index)) {
       return cache.get(index) 
    }
    if(seen.has(index)) {
        return true
    }
    seen.add(index)
    if(graph[index].length === 0) {
        result.push(index)
        cache.set(index, false)
        return false
    }
    for(let node of graph[index]) {
        let cicular = dfs(graph, node, seen, cache, result)
        if(cicular) {
            cache.set(index, true)
            return true
        }
    }
    result.push(index)
    cache.set(index, false)
    return false
    
}
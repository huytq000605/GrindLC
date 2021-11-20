function findSmallestSetOfVertices(n: number, edges: number[][]): number[] {
    let graph = new Map()
    for(let [from, to] of edges) {
        if(!graph.has(to)) graph.set(to, [])
        graph.get(to).push(from)
    }
    let result = []
    for(let i = 0; i < n; i++) {
        if(!graph.has(i) || graph.get(i).length === 0) {
            result.push(i)
        }
    }
    return result
};
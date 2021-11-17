function maximalPathQuality(values: number[], edges: number[][], maxTime: number): number {
    let graph = new Map()
    for(let edge of edges) {
        if(!graph.has(edge[0])) graph.set(edge[0], [])
        if(!graph.has(edge[1])) graph.set(edge[1], [])
        graph.get(edge[0]).push([edge[1], edge[2]])
        graph.get(edge[1]).push([edge[0], edge[2]])
    }
    let queue: any = [[0, 0, new Set()]]
    let result = 0
    while(queue.length) {
        let [node, time, set] = queue.pop()
        set.add(node)
        if(node === 0) {
            let res = 0
            for(let pass of set.values()) {
                res += values[pass]
            }
            result = Math.max(result, res)
        }
        if(graph.has(node)) {
            for(let [nextNode, timeTake] of graph.get(node)) {
                if(time + timeTake > maxTime) continue
                queue.push([nextNode, time + timeTake, new Set(set)])
            }
        }
        
    }
        
    return result
};
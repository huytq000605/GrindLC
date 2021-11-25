function findMinHeightTrees(n: number, edges: number[][]): number[] {
    if(n === 1) return [0]
    let graph = new Map()
    let count = Array(n).fill(0)
    for(let [u, v] of edges) {
        if(!graph.has(u)) graph.set(u, [])
        if(!graph.has(v)) graph.set(v, [])
        graph.get(u).push(v)
        graph.get(v).push(u)
        count[u]++
        count[v]++
        
    }
    
    let leaves = []
    let seen = 0
    
    for(let [node, connected] of graph.entries()) { // Go from outer to inter
        if(connected.length === 1) {
            leaves.push(node)
            seen++
        }
    }
    
    while(leaves.length > 2 || n - (seen - leaves.length) > 2) { // n - (seen - leaves.length) is how many remaining nodes
        let next = []
        while(leaves.length) {
            let node = leaves.pop()
            for(let nextNode of graph.get(node)) {
                count[nextNode]--
                if(count[nextNode] === 1) {
                    next.push(nextNode)
                    seen++
                }
                
            }
        }
        leaves = next
    }
    
    return leaves
    
};
function countSubTrees(n: number, edges: number[][], labels: string): number[] {
    let graph = new Map()
    for(let edge of edges) {
        if(!graph.has(edge[0])) graph.set(edge[0], [])
        if(!graph.has(edge[1])) graph.set(edge[1], [])
        graph.get(edge[0]).push(edge[1])
        graph.get(edge[1]).push(edge[0])
    }
    let result = Array(n).fill(1)
    let seen = new Set()
    
    let dfs = (current) => {
        seen.add(current)
        let letter = Array(26).fill(0)
        letter[labels.charCodeAt(current) - "a".charCodeAt(0)]++
        if(graph.has(current)) {
            for(let connected of graph.get(current)) {
                if(seen.has(connected)) continue
                let res = dfs(connected)
                for(let i = 0; i < 26; i++) {
                    letter[i] += res[i]
                }
            }
        }
        result[current] = letter[labels.charCodeAt(current) - "a".charCodeAt(0)]
        return letter
    }
    dfs(0)
    
    return result
};
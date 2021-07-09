function isBipartite(graph: number[][]): boolean {
    let setA = new Set()
    let setB = new Set()
    let num = 0
    function dfs(node: number, isSetA: boolean) {
        num++
        if(isSetA) {
            setA.add(node)
        } else {
            setB.add(node)
        }
        for(let connected of graph[node]) {
            if(isSetA && setA.has(connected)) return false
            if(!isSetA && setB.has(connected)) return false
            if(setA.has(connected) || setB.has(connected)) continue
            if(dfs(connected, !isSetA) === false) return false // Union find
        }
        return true 
    }
    for(let i = 0; i < graph.length; i++) { 
		if(graph[i].length === 0) { // Blank node (node that doesn't connect to any other node)
            num++
        } else if(!setA.has(i) && !setB.has(i)) { // Union Find by dfs
            if(dfs(i, true) === false) return false
        } 
    }
    return num === graph.length
    
};
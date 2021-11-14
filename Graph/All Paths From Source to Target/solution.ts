function allPathsSourceTarget(graph: number[][]): number[][] {
    let path = [0]
    let result = []
    let dfs = (node) => {
        if(node === graph.length - 1) {
            result.push([...path])
            return
        }
        for(let next of graph[node]) {
            path.push(next)
            dfs(next)
            path.pop()
        }
    }
    
    dfs(0)
    return result
};
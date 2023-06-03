function numOfMinutes(n: number, headID: number, manager: number[], informTime: number[]): number {
    let graph = new Map()
    let head = 0
    for(let i = 0; i <  manager.length; i++) {
        if(manager[i] === -1) {
            head = i
        }
        if(!graph.has(manager[i])) graph.set(manager[i], [])
        graph.get(manager[i]).push(i)
    }
    
    let dfs = (current) => {
        if(!graph.has(current)) return 0
        let result = 0
        for(let connect of graph.get(current)) {
            result = Math.max(result, informTime[current] + dfs(connect))
        }
        return result
    }
    return dfs(head)
};
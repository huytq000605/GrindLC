function findCircleNum(isConnected: number[][]): number {
    let seen = Array(isConnected.length).fill(false)
    let result = 0
    
    let dfs = (node) => {
        seen[node] = true
        let connected = isConnected[node]
        for(let i = 0; i < connected.length; i++) {
            if(connected[i] === 1 && !seen[i]) {
                dfs(i)
            }
        }
    }
    
    for(let i = 0; i < isConnected.length; i++) {
        if(seen[i]) continue
        dfs(i)
        result++
    }
    
    return result
    
};
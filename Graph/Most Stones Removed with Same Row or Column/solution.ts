function removeStones(stones: number[][]): number {
    let used = Array(removeStones.length)
    let island = 0
    let dfs = ([i, j]: any) => {
        for(let k = 0; k < stones.length; k++) {
            if(used[k] !== undefined) continue
            if(stones[k][0] === i || stones[k][1] === j) {
                used[k] = true
                dfs(stones[k])
            }
        }
    }
    
    for(let i = 0; i < stones.length; i++) {
        if(used[i] !== undefined) continue
        used[i] = true
        dfs(stones[i])
        island++
    }
    
    return stones.length - island
};
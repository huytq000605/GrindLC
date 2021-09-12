function smallestMissingValueSubtree(parents: number[], nums: number[]): number[] {
    let graph = new Map()
    for(let i = 1; i < parents.length; i++) {
        if(!graph.has(parents[i])) {
            graph.set(parents[i], [])
        }
        graph.get(parents[i]).push(i)
    }
    let result = Array(parents.length).fill(1)
    let seen = new Set()
    let seenVal = new Set()
    let missing = 1
    
    let dfs = (current) => {
        if(!seen.has(current)) {
            seenVal.add(nums[current])
            seen.add(current)
            while(seenVal.has(missing)) {
                missing++
            }
            if(graph.has(current)) {
                for(let child of graph.get(current)) {
                    dfs(child)
                }
            }
            return missing
        }
    }
    
    // Only need to calculate from root to where node where nums[node] == 1
    let current = nums.indexOf(1)
    
    while(current !== -1) {
        result[current] = dfs(current)
        current = parents[current]
    }
    
    return result
    
    
};
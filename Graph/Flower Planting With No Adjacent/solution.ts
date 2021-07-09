function gardenNoAdj(n: number, paths: number[][]): number[] {
    let result = Array(n + 1).fill(-1)
    let graph = new Map()
    for(let path of paths) {
        if(!graph.get(path[0])) graph.set(path[0], [])
        if(!graph.get(path[1])) graph.set(path[1], [])
        graph.get(path[0]).push(path[1])
        graph.get(path[1]).push(path[0])
    }
    for(let i = 1; i <= n; i++) {
        if(!graph.has(i)) {
            result[i] = 1
            continue
        }
        let flowerUsed = Array(5).fill(0)
        
        for(let connect of graph.get(i)) {
            if(result[connect] !== -1) {
                flowerUsed[result[connect]] = 1
            }
        }
        for(let j = 1; j < flowerUsed.length; j++) {
            if(flowerUsed[j] === 0) {
                result[i] = j
            }
        }
    }
        
    result.shift()
    return result
    
};

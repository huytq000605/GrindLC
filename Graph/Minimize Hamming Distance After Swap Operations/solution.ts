function minimumHammingDistance(source: number[], target: number[], allowedSwaps: number[][]): number {
    let result = 0
    let graph = new Map()
    for(let pair of allowedSwaps) {
        if(!graph.has(pair[0])) graph.set(pair[0], [])
        if(!graph.has(pair[1])) graph.set(pair[1], [])
        graph.get(pair[0]).push(pair[1])
        graph.get(pair[1]).push(pair[0])
    }
    let seen = new Set()

    function dfs(current: number, group: number[]) {
        seen.add(current)
        group.push(current)
        for(let connected of graph.get(current)) {
            if(seen.has(connected)) continue
            dfs(connected, group)
        }
    }
    for(let i = 0; i < source.length; i++) {
        if(!graph.has(i)) {
            if(source[i] !== target[i]) result++
        } else {
            let group = []
            let targetValue = new Map()
            let sourceValue = new Map()
            if(!seen.has(i)) dfs(i, group)
            for(let idx of group) {
                sourceValue.set(source[idx], (sourceValue.get(source[idx]) || 0) + 1)
                targetValue.set(target[idx], (targetValue.get(target[idx]) || 0) + 1)
            }
            for(let [key, value] of targetValue.entries()) {
                if(!sourceValue.has(key)) {
                    result += value
                }
                if(sourceValue.get(key) < value) {
                    result += value - sourceValue.get(key)
                }
            }
            
        }
    }
    return result
};
function shortestAlternatingPaths(n: number, red_edges: number[][], blue_edges: number[][]): number[] {
    let redGraph = new Map()
    let blueGraph = new Map()
    for(let edge of red_edges) {
        if(!redGraph.has(edge[0])) redGraph.set(edge[0], [])
        redGraph.get(edge[0]).push(edge[1])
    }
    
    for(let edge of blue_edges) {
        if(!blueGraph.has(edge[0])) blueGraph.set(edge[0], [])
        blueGraph.get(edge[0]).push(edge[1])
    }
    
    let cache = Array(n).fill(0).map(() => Array(2))
    let result = Array(n).fill(-1)
    result[0] = 0
    let queue = [[0, 0, 0], [0, 1, 0]]
    while(queue.length) {
        let [current, color, distance] = queue.shift()
        if(result[current] > distance || result[current] === -1) {
            result[current] = distance
        }
        cache[current][color] = 1
        if(color === 0) {
            if(blueGraph.has(current)) {
                for(let connect of blueGraph.get(current)) {
                    if(cache[connect][1] !== undefined) continue
                    queue.push([connect, 1, distance + 1])
                }
            }
        } else {
            if(redGraph.has(current)) {
                for(let connect of redGraph.get(current)) {
                    if(cache[connect][0] !== undefined) continue
                    queue.push([connect, 0, distance + 1])
                }
            }
        }
    }
    return result
};
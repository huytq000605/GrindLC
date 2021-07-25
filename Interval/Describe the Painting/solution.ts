function splitPainting(segments: number[][]): number[][] {
    let change = new Set()
    let color = Array(100000 + 1).fill(0)
    for(let segment of segments) {
        change.add(segment[0])
        change.add(segment[1])
        color[segment[0]] += segment[2]
        color[segment[1]] -= segment[2]
    }
    let result = []
    let sum = 0
    for(let i = 1; i < color.length; i++) {
        sum += color[i]
        if(change.has(i)) {
            if(!result.length) result.push([i, -1, sum])
            else {
                result[result.length - 1][1] = i
                if(result[result.length - 1][2] === 0) result.pop()
                result.push([i, - 1, sum])
            }
        }
        
    }
    if (result[result.length - 1][1] === -1) {
        result.pop()
    }
    return result
};
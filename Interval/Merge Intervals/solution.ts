function merge(intervals: number[][]): number[][] {
    intervals.sort((a,b) => a[0] - b[0] || a[1] - b[1])
    let result = [intervals[0]]
    for(let [index, interval] of intervals.entries()) {
        if(index === 0) continue
        if(interval[0] > result[result.length - 1][1]) {
            result.push(interval)
        } else {
            let lastResult = result[result.length - 1]
            result[result.length - 1] = [Math.min(lastResult[0], interval[0]), Math.max(lastResult[1], interval[1])]
        }
    }
    return result
};
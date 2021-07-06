function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a,b) => a[0] - b[0] || a[1] - b[1])
    let result = 0;
    let end = intervals[0][1]
    for(let i = 1; i < intervals.length; i++) {
        if(intervals[i][0] < end) {
            result++
            end = Math.min(end, intervals[i][1])
        } else {
            end = intervals[i][1]
        }
    }
    return result
};
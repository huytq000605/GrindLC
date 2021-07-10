function findRightInterval(intervals: number[][]): number[] {
    intervals = intervals.map((interval, idx) => [...interval, idx]).sort((a,b) => a[0]-b[0])
    let result = Array(intervals.length).fill(-1)
    for(let i = 0; i < intervals.length; i++) {
        if(intervals[i][0] === intervals[i][1]) {
            result[intervals[i][2]] = intervals[i][2]
            continue
        }
        let min = i + 1
        let max = intervals.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min)/ 2)
            if(intervals[mid][0] < intervals[i][1]) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        if(min < intervals.length && intervals[min][0] >= intervals[i][1]) {
            result[intervals[i][2]] = intervals[min][2]
        }
    }
    return result
};

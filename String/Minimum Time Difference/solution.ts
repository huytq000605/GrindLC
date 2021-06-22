function findMinDifference(timePoints: string[]): number {
    timePoints.sort()
    let result = 9999
    for(let i = 1; i < timePoints.length; i++) {
        result = Math.min(result, diffMin(timePoints[i-1], timePoints[i]))
    }
    result = Math.min(result, diffMin(timePoints[0] ,timePoints[timePoints.length - 1]))
    return result
};

function diffMin(tp1, tp2) {
    let hour1 = Number(tp1.slice(0,2))
    let min1 = Number(tp1.slice(3))
    let hour2 = Number(tp2.slice(0,2))
    let min2 = Number(tp2.slice(3))
    let diff = (hour2 - hour1) * 60 + min2 - min1
    if(diff > 720) {
        return 1440 - diff
    }
    return diff
}
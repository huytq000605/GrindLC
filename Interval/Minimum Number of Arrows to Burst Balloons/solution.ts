function findMinArrowShots(points: number[][]): number {
    points.sort((a,b) => a[0] - b[0] || a[1]-b[1])
    let result = 1
    let end = points[0][1]
    for(let [i, point] of points.entries()) {
        if(i === 0) continue
        if(point[0] > end) {
            result++
            end = point[1]
        } else {
            end = Math.min(end, point[1])
        }
    }
    return result
};
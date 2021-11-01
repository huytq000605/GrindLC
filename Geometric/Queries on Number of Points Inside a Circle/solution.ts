function countPoints(points: number[][], queries: number[][]): number[] {
    points.sort((a,b) => a[0]-b[0])
    let lowerBound = (centerX, r) => {
        let min = 0
        let max = points.length - 1
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            let point = points[mid]
            if(point[0] < centerX - r) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        return min
    }
    let result = Array(queries.length).fill(0)
    for(let i = 0; i < queries.length; i++) {
        let query = queries[i]
        let center = [query[0], query[1]]
        let r = query[2]
        let minIndex = lowerBound(center[0], r)
        for(let j = minIndex; j < points.length; j++) {
            if(center[0] + r < points[j][0]) break
            if(distance(center, points[j]) <= r) {
                result[i]++
            } 
            
        }
        
    }
    return result
};

function distance(point1, point2) {
    let xDiff = point1[0] - point2[0]
    let yDiff = point1[1] - point2[1]
    return Math.sqrt(xDiff * xDiff + yDiff * yDiff)
}

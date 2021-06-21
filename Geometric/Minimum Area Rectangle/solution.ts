function minAreaRect(points: number[][]): number {
    let pointMap = new Map()
    for(let point of points) {
        let x = point[0]
        let y = point[1]
        pointMap.set(`${x}-${y}`, true)
    }
    let result = Number.MAX_SAFE_INTEGER
    let hasRectangle = false
    for(let point1 of points) {
        for(let point2 of points) {
            if(point2[0] === point1[0] || point2[1] === point1[1]) continue
            let x1 = point1[0]
            let y1 = point1[1]
            let x2 = point2[0]
            let y2 = point2[1]
            if(pointMap.has(`${x1}-${y2}`) && pointMap.has(`${x2}-${y1}`)) {
                hasRectangle = true
                let area = Math.abs(x1 - x2) * Math.abs(y1 - y2)
                if(area < result) result = area
            }
        }
    }
    if(!hasRectangle) return 0
    return result
};
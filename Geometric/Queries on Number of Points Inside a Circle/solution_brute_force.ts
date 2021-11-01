function countPoints(points: number[][], queries: number[][]): number[] {
    let result = Array(queries.length).fill(0)
    for(let i = 0; i < queries.length; i++) {
        let query = queries[i]
        let center = [query[0], query[1]]
        let r = query[2]
        for(let point of points) {
            if(distance(point, center) <= r) {
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
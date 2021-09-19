function findMaxValueOfEquation(points: number[][], k: number): number {
    let result = Number.MIN_SAFE_INTEGER
    let deque = []
    for(let i = 0; i < points.length; i++) {
        while(deque.length && points[i][0] - deque[0][0] > k) {
            deque.shift()
        }
        if(deque.length) {
            let prev = deque[0]
            result = Math.max(result, points[i][0] - prev[0] + prev[1] + points[i][1])
        }
        while(deque.length) {
            let last = deque[deque.length - 1]
            if(points[i][0] - last[0] + last[1] <= points[i][1]) {
                deque.pop()
            } else {
                break
            }
        }
        deque.push(points[i])
    }
    return result
};
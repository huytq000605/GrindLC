function carPooling(trips: number[][], capacity: number): boolean {
    let accumulator = Array(1001).fill(0)
    for(let trip of trips) {
        accumulator[trip[1]] += trip[0]
        accumulator[trip[2]] -= trip[0]
    }
    let sum = 0
    for(let i = 0; i < accumulator.length; i++) {
        sum += accumulator[i]
        if(sum > capacity) return false
    }
    return true
};
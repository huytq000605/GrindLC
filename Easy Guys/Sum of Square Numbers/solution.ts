function judgeSquareSum(c: number): boolean {
    let low = 0
    let high = Math.floor(Math.sqrt(c))
    while(low <= high) {
        let current = low * low + high * high
        if(current === c) return true
        if(current < c) {
            low++
        }
        if(current > c) {
            high--
        }
    }
    return false
};
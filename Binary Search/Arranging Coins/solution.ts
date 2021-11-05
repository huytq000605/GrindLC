function arrangeCoins(n: number): number {
    // ((row + 1) * (row) / 2) < n
    let min = 0
    let max = 2 ** 31 - 1
    while(min < max) {
        let mid = min + Math.ceil((max - min + 1) / 2)
        if(((mid + 1) * mid / 2) <= n) {
            min = mid
        } else {
            max = mid - 1
        }
    }
    return min
};
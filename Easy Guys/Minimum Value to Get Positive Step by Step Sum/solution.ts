function minStartValue(nums: number[]): number {
    let min = Number.MAX_SAFE_INTEGER
    let sum = 0
    for(let num of nums) {
        sum += num
        min = Math.min(min, sum)
    }
    return 1 - Math.min(0, min)
};
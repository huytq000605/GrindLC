function increasingTriplet(nums: number[]): boolean {
    let a = Number.MAX_SAFE_INTEGER
    let b = Number.MAX_SAFE_INTEGER
    for(let num of nums) {
        if(num > b) return true
        if(num <= a) {
            a = num
        } else if(num < b) {
            b = num
        }
    }
    return false
};
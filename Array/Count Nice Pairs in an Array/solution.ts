function countNicePairs(nums: number[]): number {
    let map = new Map()
    let MOD = 1e9 + 7
    let result = 0
    for(let num of nums) {
        let revNum = rev(num)
        let diff = revNum - num
        if(map.has(diff)) {
            result += map.get(diff) 
            result = result % MOD
        }
        map.set(diff, (map.get(diff) || 0) + 1)
    }
    return result
};

function rev(num: number) {
    let result = 0
    while(num > 0) {
        let lastNumber = num % 10
        num = Math.floor(num / 10)
        result = result * 10 + lastNumber
    }
    return result
}
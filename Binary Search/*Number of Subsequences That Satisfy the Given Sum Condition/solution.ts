function numSubseq(nums: number[], target: number): number {
    let MOD = 1e9 + 7
    let result = 0
    nums.sort((a,b) => a-b)
    let cache = Array(nums.length)
    let countSubsequence = (num) => {
        if(num === 1) return 1
        if(cache[num] !== undefined) return cache[num]
        cache[num] = (countSubsequence(num - 1) * 2) % MOD
        return cache[num]
    }
    for(let i = 0; i < nums.length; i++) {
        let min = i
        let max = nums.length - 1
        while(min < max) {
            let mid = min + Math.ceil((max - min + 1) / 2)
            if(nums[mid] + nums[i] > target) {
                max = mid - 1
            } else {
                min = mid
            }
        }
        if(nums[i] + nums[min] <= target) {
            result += countSubsequence(min - i + 1)
            result = result % MOD
        }
    }
    return result
};
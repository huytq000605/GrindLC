function sumOfFlooredPairs(nums: number[]): number {
    nums.sort((a,b) => a-b)
    let i = 0
    let n = nums.length
    let result = 0
    let MOD = 1e9 + 7
    while(i < n) {
        let num = nums[i]
        let freq = 0
        while(i < n && nums[i] == num) {
            i++
            freq++
        }
        result += freq * freq
        let j = i
        while(j < n) {
            let div = Math.floor(nums[j] / num)
            let start = j
            let end = n - 1
            while(start < end) {
                let mid = start + Math.ceil((end - start + 1) / 2)
                if(Math.floor(nums[mid] / num) > div) 
                    end = mid - 1
                else
                    start = mid
            }
            result += (freq * div * (start - j + 1)) % MOD
            result %= MOD
            j = start + 1
        }
    }
    return result
};
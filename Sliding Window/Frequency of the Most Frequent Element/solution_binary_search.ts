function maxFrequency(nums: number[], k: number): number {
    nums.sort((a,b) => a-b)
    let prefix = Array(nums.length).fill(0)
    prefix[0] = nums[0]
    for(let i = 1; i < nums.length; i++) {
        prefix[i] = prefix[i-1] + nums[i]
    }
    let result = 1
    for(let i = 1; i < nums.length; i++) {
        let target = nums[i] * (i + 1)
        let sum = prefix[i]
        let operations = target - sum
        if(operations <= k) {
            result = Math.max(result, i + 1)
            continue
        }
        let min = 0
        let max = i
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            let sum = prefix[i] - prefix[mid]
            let target = nums[i] * (i - (mid+1) + 1)
            let operations = target - sum
            if(operations > k) {
                min = mid + 1
            } else {
                max = mid
            }
        }
        result = Math.max(result, i - (min+1) + 1)
    }
    return result
};
function waysToSplit(nums: number[]): number {
    let prefixSum = Array(nums.length).fill(0)
    let MOD = 1e9 + 7
    for(let i = 0; i < nums.length; i++) {
        if(i > 0) prefixSum[i] = prefixSum[i-1]
        prefixSum[i] += nums[i]
    }
    
    let result = 0
    let left = 0
    let right = 0
    
    for(let end1 = 0; end1 < nums.length - 2; end1++) {
        let leftSum = prefixSum[end1]
        left = Math.max(end1 + 1, left)
        while(left < nums.length - 1 && prefixSum[left] - leftSum < leftSum) {
            left++
        }
        if(prefixSum[left] - leftSum < leftSum || prefixSum[nums.length - 1] - prefixSum[left] < prefixSum[left] - leftSum) continue
        right = Math.max(right, left)
        while(right < nums.length - 2 && prefixSum[nums.length - 1] - prefixSum[right] >= prefixSum[right] - leftSum) {
            right++
        }
        if(prefixSum[nums.length - 1] - prefixSum[right] < prefixSum[right] - leftSum) right--
        result += right - left + 1
        result = result % MOD
        
    }
    return result
};
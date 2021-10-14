function waysToSplit(nums: number[]): number {
    let prefixSum = Array(nums.length).fill(0)
    let MOD = 1e9 + 7
    for(let i = 0; i < nums.length; i++) {
        if(i > 0) prefixSum[i] = prefixSum[i-1]
        prefixSum[i] += nums[i]
    }
    
    let result = 0
    for(let end1 = 0; end1 < nums.length - 2; end1++) {
        let leftSum = prefixSum[end1]
        
        let left
        let min = end1 + 1
        let max = nums.length - 2
        while(min < max) {
            let mid = min + Math.floor((max - min) / 2)
            let middleSum = prefixSum[mid] - leftSum
            if(leftSum <= middleSum) {
                max = mid
            } else {
                min = mid + 1
            }
        }
        left = min
        let middleSum = prefixSum[left] - leftSum
        if(leftSum > middleSum) continue
        
        let right
        min = left
        max = nums.length - 2
        while(min < max) {
            let mid = min + Math.ceil((max - min + 1) / 2)
            let middleSum = prefixSum[mid] - leftSum
            let rightSum = prefixSum[nums.length - 1] - prefixSum[mid]
            if(middleSum <= rightSum) {
                min = mid
            } else {
                max = mid - 1
            }
        }
        right = min
        middleSum = prefixSum[right] - leftSum
        let rightSum = prefixSum[nums.length - 1] - prefixSum[right]
        if(middleSum > rightSum) continue
        result += right - left + 1
        result = result % MOD
    }
    return result
};
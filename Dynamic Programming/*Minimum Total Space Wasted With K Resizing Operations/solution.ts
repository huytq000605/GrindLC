function minSpaceWastedKResizing(nums: number[], k: number): number {
    let cache = Array(nums.length).fill(0).map(() => Array(k))
    
    let prefixSum = Array(nums.length)
    for(let i = 0; i < nums.length; i++) {
        if(i === 0) prefixSum[i] = nums[i]
        else prefixSum[i] = prefixSum[i - 1] + nums[i]
    }
    let helper = (index: number, resize: number) => { // We recursive to try everything so O(time) will be O(nums.length^2 * k)
        if(index === nums.length) return 0 // We set all the size for dynamic array so just return
        if(resize < 0) return Number.MAX_SAFE_INTEGER // We have no more resize for next time then we return the maximum
        if(cache[index][resize] !== undefined) return cache[index][resize]
        let max = nums[index]
        let result = Number.MAX_SAFE_INTEGER
        // O(n) here
        for(let i = index; i < nums.length; i++) { // Think about we select a size of dynamic array for time [index, i]
            max = Math.max(max, nums[i])
            let sum: number
            if(index === 0) {
                sum = prefixSum[i]
            } else {
                sum = prefixSum[i] - prefixSum[index - 1]
            }
            let wasted = max*(i - index + 1) - sum
            // O(n*k) here
            result = Math.min(result, helper(i + 1, resize - 1) + wasted)
        }
        cache[index][resize] = result
        return result
    }
    return helper(0, k)
};
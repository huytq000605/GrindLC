function minOperations(nums: number[]): number {
    let diff = nums.length - 1
    nums.sort((a,b) => a-b)
    let longestFit = 0 // Longest length of subarray that fit the condition already
    let needChangeInside = new Set() // Same number so must change
    let start = 0
    let seen = new Set()
    for(let i = 0; i < nums.length; i++) {
        while(nums[i] - nums[start] > diff) {
            if(seen.has(nums[start])) seen.delete(nums[start])
            if(needChangeInside.has(start)) needChangeInside.delete(start)
            start++
        }
        if(seen.has(nums[i])) needChangeInside.add(i)
        seen.add(nums[i])
        longestFit = Math.max(longestFit, i - start + 1 - needChangeInside.size)
    }
    return nums.length - longestFit
};
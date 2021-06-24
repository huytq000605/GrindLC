// O(n) Space but more faster than solution2

function maximumUniqueSubarray(nums: number[]): number {
    let map = new Map()
    let result = 0;
    let start = 0
    let prefixSum = Array(nums.length).fill(0)
    for(let i = 0 ; i < nums.length; i++) {
        if(map.has(nums[i]) && map.get(nums[i]) >= start) {
            start = map.get(nums[i])
        }
		map.set(nums[i], i)

        if(i === 0) {
            prefixSum[i] = nums[i]
        } else {
            prefixSum[i] = prefixSum[i-1] + nums[i]
        }

        if(start === 0) {
			result = Math.max(result, prefixSum[i])
        } else {
            result = Math.max(result, prefixSum[i] - prefixSum[start - 1])
        }
        
    }
    return result
};
function largestSumOfAverages(nums: number[], k: number): number {
    let prefixSum = Array(nums.length).fill(0)
	// I stored a prefix sum of nums to find sum of a sub contiguous subarray in O(1)
    for(let i = 0; i < nums.length; i++) {
        prefixSum[i] = ( prefixSum[i-1] || 0 ) + nums[i]
    }
    let cache = new Map() // memoization
    let result = helper(prefixSum, k, 0, cache)
    return result
};

function helper(prefixSum: number[], numOfPartitions: number, startingIndex: number, cache: Map<string, number>) {
    if(startingIndex >= prefixSum.length) {
        return 0
    }
    if(numOfPartitions === 1) { // If this is the last partition 
        return (prefixSum[prefixSum.length - 1] - (prefixSum[startingIndex - 1] || 0) ) / (prefixSum.length - startingIndex)
    }
    const key = `${numOfPartitions}-${startingIndex}`
    if(cache.has(key)) {
        return cache.get(key)
    }
    let result = 0
    for(let i = startingIndex; i < prefixSum.length; i++) { // partitioning, choosing i as end of this partition
        let currentPartition = ( prefixSum[i] - (prefixSum[startingIndex - 1] || 0) ) / (i - startingIndex + 1)
        let nextPartition = helper(prefixSum, numOfPartitions - 1, i +1, cache)
        if(nextPartition === 0) continue
        result = Math.max(result, currentPartition + nextPartition)
    }
    cache.set(key, result)
    return result
    
}
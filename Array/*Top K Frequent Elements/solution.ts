function topKFrequent(nums: number[], k: number): number[] {
    let freqMap = new Map()
    let result = []
    for(let num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0)  + 1)
    }
	// Bucket sort
	// Since each element have max freq = nums.length
    let buckets = Array(nums.length + 1).fill(0).map(() => [])
    for(let [key, freq] of freqMap.entries()) {
        buckets[freq].push(key)
    }
    for(let i = nums.length; i > 0 && result.length < k; i--) {
        result.push(...buckets[i])
    }
    return result
};
function longestSubarray(nums: number[], limit: number): number {
    let minDequeue = []
    let maxDequeue = []
    let result = 0
    let start = 0
    for(let end = 0; end < nums.length; end++) {
        while(maxDequeue.length && nums[end] > nums[maxDequeue[maxDequeue.length - 1]]) {
            maxDequeue.pop()
        }
        while(minDequeue.length && nums[end] < nums[minDequeue[minDequeue.length - 1]]) {
            minDequeue.pop()
        }
        maxDequeue.push(end)
        minDequeue.push(end)
        while(nums[maxDequeue[0]] - nums[minDequeue[0]] > limit) {
            if(start === maxDequeue[0]) maxDequeue.shift()
            if(start === minDequeue[0]) minDequeue.shift()
            start++
        }
        result = Math.max(result, end - start + 1)
    }
    return result
};
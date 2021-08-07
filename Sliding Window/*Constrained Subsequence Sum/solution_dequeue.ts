
function constrainedSubsetSum(nums: number[], k: number): number {
    let dequeue = [] // We maintaining the maximum sum from end - k + 1 to end by this dequeue
    let result = Number.MIN_SAFE_INTEGER
    for(let i = 0; i < nums.length; i++) {
        if(dequeue.length) { // We only need to check for the first item in dequeue to make sure it contains element out of range
            if(i - dequeue[0][0] > k) {
                dequeue.shift()
            }
        }
        let bePushed = nums[i]
        if(dequeue.length) {
            bePushed = Math.max(nums[i], nums[i] + dequeue[0][1])
        }
        // Next element to be pushed must be new start or max sum from previous + current, we get the maximum
        while(dequeue.length && bePushed >= dequeue[dequeue.length - 1][1]) { // We maintain a maximum sum for next element to choose
            dequeue.pop()
        }
        dequeue.push([i, bePushed])
        
        result = Math.max(result, bePushed)
    }
    return result
};
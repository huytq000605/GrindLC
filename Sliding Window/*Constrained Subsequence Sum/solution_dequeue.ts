function constrainedSubsetSum(nums: number[], k: number): number {
    let dequeue = []
    let result = Number.MIN_SAFE_INTEGER
    for(let i = 0; i < nums.length; i++) {
        if(dequeue.length) {
            if(i - dequeue[0][0] > k) {
                dequeue.shift()
            }
        }
        let bePushed = 0
        if(dequeue.length) {
            bePushed = Math.max(nums[i], nums[i] + dequeue[0][1])
        } else {
            bePushed = nums[i]
        }
        while(dequeue.length && bePushed >= dequeue[dequeue.length - 1][1]) {
            dequeue.pop()
        }
        dequeue.push([i, bePushed])
        
        result = Math.max(result, bePushed)
    }
    return result
};
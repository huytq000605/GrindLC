function maxSlidingWindow(nums: number[], k: number): number[] {
    let dequeue = []
    let result = Array(nums.length - k + 1)
    for(let end = 0; end < nums.length; end++) {
        while(dequeue.length && nums[end] > nums[dequeue[dequeue.length - 1]]) {
            dequeue.pop()
        }
        dequeue.push(end)
        if(end - dequeue[0] + 1 > k) {
            dequeue.shift()
        }
        if(end >= k - 1) {
            result[end - k + 1] = nums[dequeue[0]]
        }
         
    }
    return result
};

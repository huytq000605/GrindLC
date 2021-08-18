function maxResult(nums: number[], k: number): number {
    let dp = Array(nums.length)
    let maxHeap = new MaxHeap((a,b) => {
        if(a[0]>b[0]) return 1
        if(a[0]===b[0]) return 0
        return -1
    })
    maxHeap.push([nums[0], 0])
    dp[0] = nums[0]
    for(let i = 1; i < nums.length; i++) {
        while(i - maxHeap.peek()[1] > k) {
            maxHeap.pop()
        }
        dp[i] = maxHeap.peek()[0] + nums[i]
        maxHeap.push([dp[i], i])
    }
    return dp[nums.length - 1]
};


class MaxHeap {
    arr
    cmp
    constructor(cmp) {
        this.arr = []
        this.cmp = cmp
    }
    
    get length() {
        return this.arr.length
    }
    
    peek() {
        return this.arr[0]
    }
    
    push(val) {
        this.arr.push(val)
        this.bubbleUp()
    }
    
    pop() {
        [this.arr[0], this.arr[this.arr.length - 1]] = [this.arr[this.arr.length - 1], this.arr[0]];
        this.arr.pop()
        this.bubbleDown()
    }
    
    bubbleUp() {
        let current = this.arr.length - 1
        while(current > 0) {
            let parent = Math.ceil(current / 2) - 1
            if(this.cmp(this.arr[current], this.arr[parent]) === 1) {
                [this.arr[current], this.arr[parent]] = [this.arr[parent], this.arr[current]]
                current = parent
            } else {
                break
            }
        }
    }
    
    bubbleDown() {
        let current = 0
        while(true) {
            let leftChild = current * 2 + 1
            if(leftChild >= this.arr.length) return
            let rightChild = leftChild + 1
            if(rightChild >= this.arr.length) rightChild = leftChild
            let bigger
            if(this.cmp(this.arr[leftChild], this.arr[rightChild]) === 1) {
                bigger = leftChild
            } else {
                bigger = rightChild
            }
            if(this.cmp(this.arr[bigger], this.arr[current]) === 1) {
                [this.arr[bigger], this.arr[current]] = [ this.arr[current], this.arr[bigger]];
                current = bigger
            } else {
                break
            }
        }
    }
}
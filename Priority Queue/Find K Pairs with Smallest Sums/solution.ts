function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    let minHeap = new MinHeap((a,b) => {
        if(a[0] + a[1] > b[0] + b[1]) return 1
        if(a[0] + a[1] === b[0] + b[1]) return 0
        return -1
    })
    for(let i = 0; i < nums1.length; i++) {
        minHeap.push([nums1[i], nums2[0], 0])
    }
    let result = []
    while(result.length < k && minHeap.length) {
        let [num1, num2, idx2] = minHeap.pop()
        result.push([num1, num2])
        if(idx2 < nums2.length - 1) {
            minHeap.push([num1, nums2[idx2 + 1], idx2 + 1])
        }
    }
    return result
};

class MinHeap {
    arr
    cmp
    
    constructor(cmp) {
        this.cmp = cmp
        this.arr = []
    }
    
    get length() {
        return this.arr.length
    }
    
    push(val) {
        this.arr.push(val)
        this.bubbleUp()
    }
    
    pop() {
        [this.arr[this.arr.length - 1], this.arr[0]] = [this.arr[0], this.arr[this.arr.length - 1]]
        const result = this.arr.pop()
        this.bubbleDown()
        return result
    }
    
    bubbleUp() {
        let current = this.arr.length - 1
        while(current > 0) {
            let parent = Math.floor((current - 1) / 2)
            if(this.cmp(this.arr[current], this.arr[parent]) === -1) {
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
            let left = current * 2 + 1
            if(left >= this.arr.length) return
            let right = left + 1
            if(right >= this.arr.length) right = left
            let smaller
            if(this.cmp(this.arr[left], this.arr[right]) === -1) {
                smaller = left
            } else {
                smaller = right
            }
            if(this.cmp(this.arr[smaller], this.arr[current]) === -1) {
                [this.arr[current], this.arr[smaller]] = [this.arr[smaller], this.arr[current]]
                current = smaller
            } else {
                break
            }
        }
        
    }
}
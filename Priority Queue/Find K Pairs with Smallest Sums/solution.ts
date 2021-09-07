function kSmallestPairs(nums1: number[], nums2: number[], k: number): number[][] {
    let first = [0, 0, nums1[0], nums2[0]]
    let result = []
    let minHeap = new MinHeap((a,b) => {
        let sum1 = a[2] + a[3]
        let sum2 = b[2] + b[3]
        if(sum1 > sum2) return 1
        if(sum1 === sum2) return 0
        return -1
    })
    minHeap.push(first)
    let seen = new Set()
    while(result.length < k && minHeap.length) {
        let [i, j, u, v] = minHeap.pop()
        result.push([u, v])
        if(i < nums1.length - 1 && !seen.has(`${i + 1},${j}`)) {
            minHeap.push([i + 1, j, nums1[i + 1], nums2[j]])
            seen.add(`${i + 1},${j}`)
        }
        if(j < nums2.length -1 && !seen.has(`${i},${j + 1}`)) {
            minHeap.push([i, j + 1, nums1[i], nums2[j + 1]])
            seen.add(`${i},${j + 1}`)
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
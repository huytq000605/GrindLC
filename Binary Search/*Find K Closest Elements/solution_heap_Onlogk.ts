function findClosestElements(arr: number[], k: number, x: number): number[] {
    let minHeap = new MinHeap()
    for(let ele of arr) {
        if (minHeap.length < k) {
            minHeap.push([ele, Math.abs(x - ele)]);
        } else {
            const peek = minHeap.peek();
            if (peek[1] > Math.abs(x - ele)) {
                minHeap.pop();
                minHeap.push([ele, Math.abs(x - ele)]);
            }
        }
    }
    let result = Array(k)
    for(let i = 0; i < result.length; i++) {
        result[i] = minHeap.heap[i][0]
    }
    result.sort((a,b) => a-b)
    return result
};

type HeapNode = [number, number]

class MinHeap {
    heap
    
    constructor() {
        this.heap = []
    }
    
    get length() {
        return this.heap.length
    }
    
    push(heapNode: HeapNode) {
        this.heap.push(heapNode)
        this.bubbleUp()
    }
    
    peek() {
        if(!this.heap.length) {
            throw new Error("No element")
        }
        return this.heap[0]
    }
    
    pop() {
        if(!this.heap.length) {
            throw new Error("No element")
        }
        [this.heap[0], this.heap[this.heap.length - 1]] = [this.heap[this.heap.length - 1], this.heap[0]]
        const pop = this.heap.pop()
        this.bubbleDown()
        return pop
    }
    
    bubbleUp() {
        let current = this.heap.length - 1
        while(current > 0) {
            let parent = Math.ceil(current / 2) - 1
            if(this.compare(this.heap[current], this.heap[parent]) === 1) {
                [this.heap[current], this.heap[parent]] = [this.heap[parent], this.heap[current]]
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
            let right = left + 1
            if(left >= this.heap.length) {
                return
            }
            if(right >= this.heap.length) {
                right = left
            }
            let bigger
            if(this.compare(this.heap[left], this.heap[right]) === 1) {
                bigger = left
            } else {
                bigger = right
            }
            if(this.compare(this.heap[bigger], this.heap[current]) === 1) {
                [this.heap[bigger], this.heap[current]] = [this.heap[current], this.heap[bigger]]
                current = bigger
            } else {
                break
            }
        }
    }
    
    compare(a, b) {
        if(a[1] > b[1]) {
            return 1
        }
        if(a[1] < b[1]) {
            return -1
        }
        return 0
    }
}

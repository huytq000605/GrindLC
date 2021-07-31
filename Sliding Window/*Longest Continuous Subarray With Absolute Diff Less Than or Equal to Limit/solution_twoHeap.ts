function longestSubarray(nums: number[], limit: number): number {
    let minHeap = new MinHeap<any>((a,b) => {
        if(nums[a] > nums[b]) return 1
        if(nums[a] === nums[b]) return 0
        return -1
    })
    
    let maxHeap = new MinHeap<any>((a,b) => {
        if(nums[a] > nums[b]) return -1
        if(nums[a] === nums[b]) return 0
        return 1
    })
    let result = 0
    let start = 0
    for(let end = 0; end < nums.length; end++) {
        maxHeap.push(end)
        minHeap.push(end)
        while(nums[maxHeap.peek()] - nums[minHeap.peek()]  > limit) {
            if(maxHeap.peek() > minHeap.peek()) {
                start = Math.max(start, minHeap.pop() + 1)
            } else {
                start = Math.max(start, maxHeap.pop() + 1)
            }
        }
        result = Math.max(result, end - start + 1)
    }
    return result
};

class MinHeap<T> {
    private heap: T[];
    private compare: (a: T, b: T) => 1 | 0 | -1
    constructor(compareFunction: (a:T, b:T) => 1 | 0 | -1) {
        this.heap = [];
        this.compare = compareFunction
    }

	get length(): number{
		return this.heap.length
	}
	
    public peek(): T | undefined {
		if(this.length > 0)
			return this.heap[0];
		else 
			return undefined
    }

    public push(val: T) {
        this.heap.push(val);
        this.bubbleUp();
    }
    
    public pop(): T | undefined {
        if(this.length === 0) {
            return undefined
        } 
        [this.heap[0], this.heap[this.length - 1]] = [this.heap[this.length - 1],this.heap[0]]
        const pop = this.heap.pop();
        this.bubbleDown();
        return pop;
    }

    private bubbleUp(): void {
        let current = this.length - 1;
        while (current > 0) {
            let parent = Math.ceil(current / 2) - 1;
            if (this.compare(this.heap[current], this.heap[parent]) == -1) {
				[this.heap[current], this.heap[parent]] = [ this.heap[parent], this.heap[current]];
                current = parent;
            } else {
                return;
            }
        }
    }

    private bubbleDown(): void {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this.length) return;
            let right = left + 1;
            if (right >= this.length) right = left;
            let smaller: number;
            if (this.compare(this.heap[left], this.heap[right]) == -1) {
                smaller = left;
            } else {
                smaller = right;
            }
            if (this.compare(this.heap[smaller], this.heap[current]) == -1) {
                [this.heap[smaller], this.heap[current]] = [
                    this.heap[current],
                    this.heap[smaller],
                ];
                current = smaller;
            } else {
                return;
            }
        }
    }
}
// This method is easy to understand, Time complexity is O(nlog(26)) => O(n)

function leastInterval(tasks: string[], n: number): number {
    let freq = new Map()
    for(let task of tasks) {
        if(!freq.has(task)) freq.set(task, 0)
        freq.set(task, freq.get(task)+ 1)
    }
    let freqHeap = new MaxHeap()
    let cooldownTask = new MinHeap()
    let t = 0
    for(let [taskName, remaining] of freq.entries()) {
        let heapNode = new HeapNode(taskName, remaining, -1)
        freqHeap.push(heapNode)
    }
    while(freqHeap.length > 0 || cooldownTask.length > 0) {
        while(cooldownTask.length && t - cooldownTask.peek().time > n) {
            const pop = cooldownTask.pop()
            freqHeap.push(pop)
        }
        
        if(freqHeap.length) {
            const pop = freqHeap.pop()
            pop.remaining--
            pop.time = t
            if(pop.remaining > 0) {
                cooldownTask.push(pop)
            }
        }
        t++
    }
    return t
};

class HeapNode {
    taskName: string
    remaining: number
    time: number
    
    constructor(taskName, remaining, time) {
        this.taskName =  taskName
        this.remaining = remaining
        this.time = time
    }
 }

class MaxHeap {
    private heap: HeapNode[];
    private _length: number;
    constructor() {
        this.heap = [];
        this._length = 0;
    }

    get length() {
        return this._length;
    }

    public peek() {
        if (this._length > 0) return this.heap[0];
        else return undefined;
    }

    public push(val: HeapNode) {
        this.heap.push(val);
        this._length++;
        this.bubbleUp();
    }

    public pop() {
        [this.heap[0], this.heap[this._length - 1]] = [
            this.heap[this._length - 1],
            this.heap[0],
        ];
        const pop = this.heap.pop();
        this._length--;
        this.bubbleDown();
        return pop;
    }
    private bubbleUp() {
        let current = this._length - 1;
        while (current > 0) {
            let parent = Math.ceil(current / 2) - 1;
            if (this.compare(this.heap[current], this.heap[parent]) == 1) {
                [this.heap[current], this.heap[parent]] = [
                    this.heap[parent],
                    this.heap[current],
                ];
                current = parent;
            } else {
                return;
            }
        }
    }
	
    private bubbleDown() {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this._length) return;
            let right = left + 1;
            if (right >= this._length) right = left;
            let compare;
            if (this.compare(this.heap[left], this.heap[right]) == 1) {
                compare = left;
            } else {
                compare = right;
            }
            if (this.compare(this.heap[compare], this.heap[current]) == 1) {
                [this.heap[compare], this.heap[current]] = [
                    this.heap[current],
                    this.heap[compare],
                ];
                current = compare;
            } else {
                return;
            }
        }
    }

    private compare(node1: HeapNode, node2: HeapNode): number {
        if (node1.remaining > node2.remaining) {
            return 1;
        }
        if (node1.remaining == node2.remaining) {
            return 0 
        }
        return -1;
    }
}

class MinHeap {
    private heap: HeapNode[];
    private _length: number;
    constructor() {
        this.heap = [];
        this._length = 0;
    }

	get length() {
		return this._length
	}
	
    public peek() {
		if(this._length > 0)
			return this.heap[0];
		else 
			return undefined
    }

    public push(val: HeapNode) {
        this.heap.push(val);
        this._length++;
        this.bubbleUp();
    }
    
    public pop() {
        [this.heap[0], this.heap[this._length - 1]] = [this.heap[this._length - 1],this.heap[0]]
        const pop = this.heap.pop();
        this._length--;
        this.bubbleDown();
        return pop;
    }

    private bubbleUp() {
        let current = this._length - 1;
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

    private bubbleDown() {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this._length) return;
            let right = left + 1;
            if (right >= this._length) right = left;
            let compare;
            if (this.compare(this.heap[left], this.heap[right]) == -1) {
                compare = left;
            } else {
                compare = right;
            }
            if (this.compare(this.heap[compare], this.heap[current]) == -1) {
                [this.heap[compare], this.heap[current]] = [
                    this.heap[current],
                    this.heap[compare],
                ];
                current = compare;
            } else {
                return;
            }
        }
    }

    private compare(node1: HeapNode, node2: HeapNode): number {
        if (node1.time > node2.time) {
            return 1;
        }
        if (node1.time == node2.time) {
            return 0 
        }
        return -1;
    }
}

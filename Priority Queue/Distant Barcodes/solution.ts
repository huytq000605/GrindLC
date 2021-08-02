function rearrangeBarcodes(barcodes: number[]): number[] {
    let freq = new Map()
    for(let b of barcodes) {
        freq.set(b, (freq.get(b) || 0) + 1)
    }
    let heap = new MaxHeap<any>((a,b) => {
        if(a[1] > b[1]) return 1
        if(a[1] === b[1]) return 0
        return -1
    })
    for(let [key, value] of freq.entries()) {
        heap.push([key, value])
    }
    let result = []
    while(heap.length) {
        let [numToPush, freq] = heap.pop()
        if(result.length && result[result.length - 1] === numToPush) {
            let [numToPush2, freq2] = heap.pop()
            result.push(numToPush2)
            if(freq2 > 1) {
                heap.push([numToPush2, freq2 - 1])
            }
            heap.push([numToPush, freq])
        } else {
            result.push(numToPush)
            if(freq > 1) {
                heap.push([numToPush, freq - 1])
            }
        }
    }
    return result
};

class MaxHeap<T> {
    private heap: T[];
    private compare: (node1: T, node2: T) => 1 | -1 | 0;
    /**
     *
     * @param compareFunction return 1 if node 1 > node 2, return -1 if node 1 < node 2, return 0 if node1 = node2
     */
    constructor(compareFn: (node1: T, node2: T) => 1 | -1 | 0) {
        this.heap = [];
        this.compare = compareFn;
    }

    get length(): number {
        return this.heap.length;
    }

    public peek(): T | undefined {
        if (this.length > 0) return this.heap[0];
        else return undefined;
    }

    public push(node: T): void {
        this.heap.push(node);
        this.bubbleUp();
    }

    public pop(): T | undefined {
        if (this.length === 0) {
            return undefined;
        }
        [this.heap[0], this.heap[this.length - 1]] = [
            this.heap[this.length - 1],
            this.heap[0],
        ];
        const pop = this.heap.pop();
        this.bubbleDown();
        return pop;
    }

    private bubbleUp(): void {
        let current = this.length - 1;
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

    private bubbleDown(): void {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this.length) return;
            let right = left + 1;
            if (right >= this.length) right = left;
            let bigger: number;
            if (this.compare(this.heap[left], this.heap[right]) == 1) {
                bigger = left;
            } else {
                bigger = right;
            }
            if (this.compare(this.heap[bigger], this.heap[current]) == 1) {
                [this.heap[bigger], this.heap[current]] = [
                    this.heap[current],
                    this.heap[bigger],
                ];
                current = bigger;
            } else {
                return;
            }
        }
    }
}



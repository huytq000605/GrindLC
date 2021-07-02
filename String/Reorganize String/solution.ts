function reorganizeString(s: string): string {
    let freq = new Map()
    for(let i = 0; i < s.length; i++) {
        freq.set(s[i], ( freq.get(s[i]) || 0 ) + 1)
    }
    let maxHeap = new MaxHeap()
    for(let w of freq.entries()) {
        maxHeap.push(w)
    }
    let previousLetter = ""
    let result = ""
    while(maxHeap.length > 0) {
        let pop = maxHeap.pop()
        if(pop[0] === previousLetter) {
            if(maxHeap.length === 0) return ""
            let pop2nd = maxHeap.pop()
            result += pop2nd[0]
            previousLetter = pop2nd[0]
            if(pop2nd[1] !== 1) maxHeap.push([pop2nd[0], pop2nd[1] - 1])
            maxHeap.push(pop)
        } else {
            result += pop[0]
            previousLetter = pop[0]
            if(pop[1] === 1) continue
            else maxHeap.push([pop[0], pop[1] - 1])
        }
    }
    return result
    
};

type HeapNode = [string, number]


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
        if (node1[1] > node2[1]) {
            return 1;
        }
        if (node1[1] == node2[1]) {
            return 0 
        }
        return -1;
    }
}

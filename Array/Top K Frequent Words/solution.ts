/*
Noted for this problem: 
O(nlogn) is naive solution, use hash map, get from it and sort like normal
Use MaxHeap still gives O(nlogn)
Use MinHeap is optimal, O(nlogk), maintaining only top K elements in heap
*/

function topKFrequent(words: string[], k: number): string[] {
    let freq = new Map()
    let maxFreq = 0
    for(let i = 0 ; i < words.length; i++) {
        freq.set(words[i], (freq.get(words[i]) || 0 ) + 1)
        let currentFreq = freq.get(words[i])
        if(currentFreq > maxFreq) {
            maxFreq = currentFreq
        }
    }
    let result = Array(k)
    let heap = new MinHeap()
    
    for(let [key, value] of freq.entries()) {
		let heapNode: HeapNode = {
			word: key,
			freq: value
		}
		if(heap.length < k) {
			heap.push(heapNode)
		} else {
			if(heap.compare(heap.peek(), heapNode) == -1) {
				heap.pop()
				heap.push(heapNode)
			}
		}
    }
    
    for(let i = k-1; i >= 0; --i) {
        result[i] = heap.pop().word
    }
    
    return result
    
};

class HeapNode {
    word: string;
    freq: number;
}

// type HeapNode = number

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

    public compare(node1: HeapNode, node2: HeapNode): number {
        if (node1.freq > node2.freq) {
            return 1;
        }
        if (node1.freq == node2.freq) {
            return node2.word.localeCompare(node1.word);
        }
        return -1;
    }
}

class StockPrice {
    map
    cur
    max
    min
    constructor() {
        this.map = new Map()
        this.min = new MinHeap((a,b) => { // Min Heap
            if(a[1] < b[1]) return -1
            if(a[1] === b[1]) return 0
            return 1
        })
        this.max = new MinHeap((a,b) => { // Max Heap
            if(a[1] < b[1]) return 1
            if(a[1] === b[1]) return 0
            return -1
        })
        this.cur = 0 // set default value
    }

    update(timestamp: number, price: number): void {
        this.map.set(timestamp, price)
        this.cur = Math.max(this.cur, timestamp)
        this.max.push([timestamp, price])
        this.min.push([timestamp, price])   
    }

    current(): number {
        return this.map.get(this.cur)
    }

    maximum(): number {
        while(true) {
            let [timestamp, price] = this.max.peek()
            if(price === this.map.get(timestamp)) {
                return price
            } else {
                this.max.pop()
                continue
            }
        }
    }

    minimum(): number {
        while(true) {
            let [timestamp, price] = this.min.peek()
            if(price === this.map.get(timestamp)) {
                return price
            } else {
                this.min.pop()
                continue
            }
        }
    }
}

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
/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = new StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
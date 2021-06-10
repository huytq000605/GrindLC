class SeatManager {
    minHeap;
    constructor(n: number) {
        this.minHeap = new MinHeap();
        for (let i = 1; i <= n; i++) {
            this.minHeap.push(i);
        }
    }

    reserve(): number {
        return this.minHeap.pop();
    }

    unreserve(seatNumber: number): void {
        this.minHeap.push(seatNumber);
    }
}

class MinHeap {
    heap: number[];
    length: number;
    constructor() {
        this.heap = [];
        this.length = 0;
    }
    peek() {
        return this.heap[0];
    }
    push(val: number) {
        this.heap.push(val);
        this.length++;
        this.bubbleUp();
    }
    pop() {
        [this.heap[0], this.heap[this.length - 1]] = [
            this.heap[this.length - 1],
            this.heap[0],
        ];
        const pop = this.heap.pop();
        this.length--;
        this.bubbleDown();
        return pop;
    }
    bubbleUp() {
        let current = this.length - 1;
        while (current > 0) {
            let parent = Math.ceil(current / 2) - 1;
            if (this.heap[current] < this.heap[parent]) {
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
    bubbleDown() {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this.length) return;
            let right = left + 1;
            if (right >= this.length) right = left;
            let compare;
            if (this.heap[left] < this.heap[right]) {
                compare = left;
            } else {
                compare = right;
            }
            if (this.heap[compare] < this.heap[current]) {
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
}
/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */

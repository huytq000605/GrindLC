function minCost(maxTime: number, edges: number[][], passingFees: number[]): number {
    let time = Array(passingFees.length).fill(Number.MAX_SAFE_INTEGER)
    time[0] = 0
    let graph = new Map()
    for(let edge of edges) {
        if(!graph.has(edge[0])) graph.set(edge[0], [])
        if(!graph.has(edge[1])) graph.set(edge[1], [])
        graph.get(edge[0]).push([edge[1], edge[2]])
        graph.get(edge[1]).push([edge[0], edge[2]])
    }
    let minHeap = new MinHeap((a,b) => {
        if(a[2] > b[2]) {
            return 1
        }
        if(a[2] === b[2]) {
            return 0
        }
        return -1
    })
    minHeap.push([0, 0, passingFees[0]])
    while(minHeap.length > 0) { // We are making sure that we traverse with minimum cost, if we are not meeting the destination, we keep running the heap, updating the time (because we sorted the cost already)
        let [u, currentTime, currentCost] = minHeap.pop() as any
        if(u === passingFees.length - 1) {
            return currentCost
        }
        for(let [v, travel] of graph.get(u)) {
            let newCost = currentCost + passingFees[v]
            let newTime = currentTime + travel
            if(newTime > maxTime) continue
            if(newTime < time[v]) {
                time[v] = newTime
                minHeap.push([v, time[v], newCost])
            }
        }
    }
    
    return -1
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
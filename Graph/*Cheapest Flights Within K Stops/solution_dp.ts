function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
    let minHeap = new MinHeap<any>((a,b) => {
        if(a[1]>b[1]) return 1
        if(a[1] === b[1]) return 0
        return -1
    })
    
    let graph = new Map()
    for(let flight of flights) {
        if(!graph.has(flight[0])) {
            graph.set(flight[0], [])
        }
        graph.get(flight[0]).push([flight[1], flight[2]])
    }
    // dp[i][j] is for minimum distance reaching i with j stops
    let dp = Array(n).fill(0).map(() => Array(k + 2).fill(Number.MAX_SAFE_INTEGER)) 
    
    for(let i = 0; i < k; i++) {
        dp[src][i] = 0
    }
    
    minHeap.push([src, 0, 0])
    while(minHeap.length) {
        let [current, currentDist, currentStop] = minHeap.pop()
        if(current === dst) {
            return currentDist
        }
        if(graph.has(current)) {
            for(let [next, dist] of graph.get(current)) {
                let newDistance = dist + currentDist
                if(next !== dst && currentStop === k) continue
                if(newDistance < dp[next][currentStop + 1]) {
                    dp[next][currentStop + 1] = newDistance
                    minHeap.push([next, newDistance, currentStop + 1])
                }
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
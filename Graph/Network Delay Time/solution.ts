function networkDelayTime(times: number[][], n: number, k: number): number {
    let graph = new Map()
    for(let [u, v, w] of times) {
        if(!graph.has(u - 1)) graph.set(u - 1, [])
        graph.get(u - 1).push([v - 1, w])
    }
    let dist = Array(n).fill(Number.MAX_SAFE_INTEGER)
    dist[k - 1] = 0
    let queue = new MinHeap<[number, number]>((a,b) => {
        if(a[1]>b[1]) return 1
        if(a[1]===b[1]) return 0
        return -1
    })
    queue.push([k - 1, 0])
    let seen = new Set()
    seen.add(k - 1)
    while(queue.length > 0) {
        let [u, currentDistance] = queue.pop() 
        seen.add(u)
        if(seen.size === n) return Math.max(...dist)
        if(graph.has(u)) {
            for(let [v, distance] of graph.get(u)) {
                let newDistance = currentDistance + distance
                if(newDistance < dist[v]) {
                    dist[v] = newDistance
                    queue.push([v, newDistance])
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
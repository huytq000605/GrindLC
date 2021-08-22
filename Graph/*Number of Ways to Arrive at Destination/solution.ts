function countPaths(n: number, roads: number[][]): number {
    let graph = new Map()
    let MOD = 1e9 + 7
    
    for(let road of roads) {
        if(!graph.has(road[0])) graph.set(road[0], [])
        if(!graph.has(road[1])) graph.set(road[1], [])
        graph.get(road[0]).push([road[1], road[2]])
        graph.get(road[1]).push([road[0], road[2]])
    }
    let minHeap = new MinHeap<any>((a,b) => {
        if(a[1] < b[1]) return -1
        if(a[1] === b[1]) return 0
        return 1
    })
    minHeap.push([0, 0])
    
    let distance = Array(n).fill(Number.MAX_SAFE_INTEGER)
    let ways = Array(n).fill(0)
    ways[0] = 1
    distance[0] = 0
    
    while(minHeap.length) {
        let [current, currentDist] = minHeap.pop()
         if(current === n - 1) {
             return ways[current]
        }
        for(let [connect, dist] of graph.get(current)) {       
            let newDist = currentDist + dist
            if(distance[connect] >= newDist) {
                distance[connect] = newDist
                if(ways[connect] !== 0) {
                    ways[connect] = (ways[connect] + ways[current]) % MOD 
                    continue
                }  
                ways[connect] = ways[current]
                minHeap.push([connect, newDist])
            }
        }
    }
    
    return -1 // Never come here
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
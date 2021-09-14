function countRestrictedPaths(n: number, edges: number[][]): number {
    let graph = new Map()
    let MOD = 1e9 + 7
    for(let edge of edges) {
        if(!graph.has(edge[0])) graph.set(edge[0], [])
        if(!graph.has(edge[1])) graph.set(edge[1], [])
        graph.get(edge[0]).push([edge[1], edge[2]])
        graph.get(edge[1]).push([edge[0], edge[2]])
    }
    let distanceToLastNode = Array(n+1).fill(Number.MAX_SAFE_INTEGER)
    distanceToLastNode[n] = 0
    let minHeap = new MinHeap<any>((a,b) => {
        if(a[1] < b[1]) return -1
        if(a[1] === b[1]) return 0
        return 1
    })
    minHeap.push([n, 0])
    let seen = new Set()
    while(minHeap.length) {
        let [curr, currDist] = minHeap.pop()
        if(seen.has(curr)) continue
        seen.add(curr)
        if(seen.size === n) break
        if(graph.has(curr)) {
            for(let [connect, dist] of graph.get(curr)) {
                let newDistance = currDist + dist
                if(newDistance < distanceToLastNode[connect]) {
                    distanceToLastNode[connect] = newDistance
                    minHeap.push([connect, newDistance])
                }
            }
        }
    }
    let dp = Array(n+1)
    let dfs = (current) => {
        if(current === 1) {
            return 1
        }
        if(dp[current] !== undefined) return dp[current]
        let result = 0
        if(graph.has(current)) {
            for(let [connect] of graph.get(current)) {
                if(distanceToLastNode[current] < distanceToLastNode[connect]) {
                    result += dfs(connect)
                    result = result % MOD
                }
            }
        }
        dp[current] = result
        return result
    }
    return dfs(n)
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
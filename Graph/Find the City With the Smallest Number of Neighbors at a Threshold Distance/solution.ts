// Dijkstra for each node
function findTheCity(n: number, edges: number[][], distanceThreshold: number): number {
    let graph = {}
    for(let edge of edges) {
        if(!graph[edge[0]]) graph[edge[0]] = []
        if(!graph[edge[1]]) graph[edge[1]] = []
        graph[edge[0]].push([edge[1], edge[2]])
        graph[edge[1]].push([edge[0], edge[2]])
    }
    let result = undefined
    for(let start = 0; start < n; start++) {
        let distance = Array(n).fill(Number.MAX_SAFE_INTEGER)
        distance[start] = 0
        let seen = new Set()
        let queue = new MinHeap((a,b) => {
            if(a[1] - b[1] > 0) {
                return 1
            }
            if(a[1] === b[1]) return 0
            return -1
        })
        queue.push([start, 0])
        while(queue.length > 0) {
            let [u, currentDist] = queue.pop() as any
            seen.add(u)
            if(!graph[u]) continue
            for(let [v, dist] of graph[u]) {
                let newDistance = currentDist + dist
                if(newDistance > distanceThreshold) continue
                if(newDistance < distance[v]) {
                    distance[v] = newDistance
                    queue.push([v, newDistance])
                }
            }
        }
        if(!result || seen.size < result[1] || result[1] === seen.size && start > result[0]) {
            result = [start, seen.size]
        }
    }
    return result[0]
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
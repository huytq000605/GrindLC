function reachableNodes(edges: number[][], maxMoves: number, n: number): number {
    let graph = new Map()
    for(let edge of edges) {
        if(!graph.has(edge[0])) graph.set(edge[0], [])
        if(!graph.has(edge[1])) graph.set(edge[1], [])
        
        graph.get(edge[0]).push([edge[1], edge[2]])
        graph.get(edge[1]).push([edge[0], edge[2]])
    }
    let minHeap = new MinHeap<any>((a,b) => {
        if(a[1] > b[1]) return -1
        if(a[1] === b[1]) return 0
        return 1
    })
    minHeap.push([0, maxMoves])

    let remainingMoves = Array(n).fill(-1)
    remainingMoves[0] = maxMoves

    let result = 0
    let point = new Map()
    let seen = new Set()

    while(minHeap.length) {
        let [current, move] = minHeap.pop()
        if(seen.has(current)) continue
        seen.add(current)
        if(graph.has(current) && move > 0) {
            for(let [next, sub] of graph.get(current)) {
                if(sub + 1 <= move) {
                    if(!point.has(current)) point.set(current, new Map())
                    point.get(current).set(next, sub)
				
					// can go to all subdivide
                    if(point.has(next) && point.get(next).has(current)) {
                        result = result - point.get(next).get(current) + sub
                    } else {
                        result += sub
                    }

                    if(!seen.has(next) && move - sub - 1 > remainingMoves[next]) {
                        remainingMoves[next] = move - sub - 1
                        minHeap.push([next, move - sub - 1])
                    }
                } else {
                    if(!point.has(current)) point.set(current, new Map())
                    point.get(current).set(next, move)
                    let plus = move
					
					// Go from 2 side
                    if(point.has(next) && point.get(next).has(current)) {
                        plus += point.get(next).get(current)
                        if(plus > sub) { // Overlap
                            plus = sub 
                        }
                        result = result - point.get(next).get(current) + plus
                    } else { // 1 side
                        result += plus
                    }
                    

                }
                
            }
        }
    }
    
    result += seen.size
    return result
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
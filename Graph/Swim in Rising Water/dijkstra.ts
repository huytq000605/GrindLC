function swimInWater(grid: number[][]): number {
    let minHeap = new MinHeap()
    minHeap.push([0, 0, grid[0][0]])
    const dirs = [[0,1], [1,0], [-1,0], [0, -1]]
    let distance = Array(grid.length).fill(0).map(each => Array(grid[0].length).fill(Number.MAX_SAFE_INTEGER))
    distance[0][0] = grid[0][0]
    while(minHeap.length > 0) {
        let [i, j, time] = minHeap.pop()
        if(i === grid.length - 1 && j === grid[0].length - 1) {
            return time
        }
        for(let dir of dirs) {
            let x = i + dir[0]
            let y = j + dir[1]
            if(x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
                const newDistance = Math.max(time, grid[x][y])
                if(newDistance < distance[x][y]) {
                    distance[x][y] = newDistance
                    minHeap.push([x,y, newDistance])
                }
                
            }
        }
    }
    return distance[distance.length][distance[0].length - 1]
};

type HeapNode = [number, number, number]

class MinHeap {
    private heap: HeapNode[];
    constructor() {
        this.heap = [];
    }

	get length(): number{
		return this.heap.length
	}
	
    public peek() {
		if(this.length > 0)
			return this.heap[0];
		else 
			return undefined
    }

    public push(val: HeapNode) {
        this.heap.push(val);
        this.bubbleUp();
    }
    
    public pop() {
        if(this.length === 0) {
            return undefined
        } 
        [this.heap[0], this.heap[this.length - 1]] = [this.heap[this.length - 1],this.heap[0]]
        const pop = this.heap.pop();
        this.bubbleDown();
        return pop;
    }

    private bubbleUp() {
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

    private bubbleDown() {
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

    private compare(node1: HeapNode, node2: HeapNode): number {
        if (node1[2] > node2[2]) {
            return 1;
        }
        if (node1[2] == node2[2]) {
            return 0 
        }
        return -1;
    }
}
function minCost(grid: number[][]): number {
    let dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
	let distance = Array(grid.length).fill(0).map(() => Array(grid[0].length).fill(Number.MAX_SAFE_INTEGER))
    distance[0][0] = 0
    
    let minHeap = new MinHeap<any>((a,b) => {
        if(a[2] < b[2]) return -1
        if(a[2] === b[2]) return 0
        return 1
    })
    
    minHeap.push([0,0,0])
    
    while(minHeap.length) {
        let [row, col, curCost] = minHeap.pop()
        if(row === grid.length - 1 && col === grid[0].length - 1) return curCost
        for(let dir of dirs) {
            let nRow = row + dir[0]
            let nCol = col + dir[1]
            if(nRow < 0 || nRow >= grid.length || nCol < 0 || nCol >= grid[0].length) continue
            let cost = 1
			// Same direction => dont have cost to move
            if(dirs[grid[row][col] - 1][0] === dir[0] && dirs[grid[row][col] - 1][1] === dir[1]) cost = 0
            if(curCost + cost < distance[nRow][nCol]) {
                distance[nRow][nCol] = curCost + cost
                minHeap.push([nRow, nCol, curCost + cost])
            }
        }
    }
    
    return 0
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
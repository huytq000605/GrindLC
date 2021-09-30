function assignTasks(servers: number[], tasks: number[]): number[] {
    let serverQueue = new MinHeap<any>((a,b) => {
        if(a[0] > b[0]) return 1
        if(a[0] === b[0]) {
            if(a[1] > b[1]) return 1
            if(a[1] === b[1]) return 0
            if(a[1] < b[1]) return -1
        }
        return -1
    })
    for(let [index, server] of servers.entries()) {
        serverQueue.push([server, index])
    }
    let busyServer = new MinHeap<any>((a,b) => {
        if(a[2] < b[2]) return -1
        if(a[2] === b[2]) return 0
        return 1
    })
    let taskQueue = []
    let result = Array(tasks.length)
    let idxResult = 0
    let second = 0
    while(taskQueue.length || second < tasks.length) {
        while(busyServer.length && busyServer.peek()[2] <= second) {
            let [server, index] = busyServer.pop()
            serverQueue.push([server, index])
        }
        if(second < tasks.length) {
            taskQueue.push(tasks[second])
        }
        while(taskQueue.length && serverQueue.length) {
            let task = taskQueue.shift()
            let [server, index] = serverQueue.pop()
            result[idxResult++] = index
            busyServer.push([server, index, second + task])
        }
        second++
    }
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
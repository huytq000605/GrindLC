function smallestChair(times: number[][], targetFriend: number): number {
    let n = times.length
    times = times.map((time, index) => [...time, index])
    times.sort((a,b) => a[0]-b[0])
    let chairHeap = new MinHeap<any>((a,b) => {
        if(a > b) return 1
        if(a===b) return 0
        return -1
    })
    for(let i = 0; i < n; i++) {
        chairHeap.push(i)
    }
    let leaveHeap = new MinHeap<any>((a,b) => {
        if(a[1]>b[1]) return 1
        if(a[1]===b[1]) return 0
        return -1
    })
    let timeIndex = 0
    for(let time = 1; time <= 100000; time++) {
        while(leaveHeap.length && leaveHeap.peek()[1] === time) {
            chairHeap.push(leaveHeap.pop()[3])
        }
        while(timeIndex < times.length && times[timeIndex][0] === time) {
            let chair = chairHeap.pop()
            if(times[timeIndex][2] === targetFriend) {
                return chair
            }
            leaveHeap.push([...times[timeIndex], chair])
            timeIndex++
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

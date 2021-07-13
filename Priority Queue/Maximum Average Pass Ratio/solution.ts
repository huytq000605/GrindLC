function maxAverageRatio(classes: number[][], extraStudents: number): number {
    let maxHeap = new MaxHeap((a,b) => {
        let incA = (a[0] + 1)/(a[1] + 1) - a[0]/a[1]
        let incB = (b[0] + 1)/(b[1] + 1) - b[0]/b[1]
        if(incA > incB) {
            return 1
        }
        if(incA === incB) {
            return 0
        }
        return -1
    })
    let result = 0
    for(let classN of classes) {
        result += classN[0]/ classN[1]
        maxHeap.push(classN)
    }
    while(extraStudents > 0) {
        let [pass, total] = maxHeap.pop() as any
        maxHeap.push([pass + 1, total + 1])
        result += (pass + 1) / (total + 1) - pass/total
        extraStudents--
    }
    return result/classes.length
};

class MaxHeap<T> {
    private heap: T[];
    private compare: (node1: T, node2: T) => 1 | -1 | 0;
    /**
     *
     * @param compareFunction return 1 if node 1 > node 2, return -1 if node 1 < node 2, return 0 if node1 = node2
     */
    constructor(compareFn: (node1: T, node2: T) => 1 | -1 | 0) {
        this.heap = [];
        this.compare = compareFn;
    }

    get length(): number {
        return this.heap.length;
    }

    public peek(): T | undefined {
        if (this.length > 0) return this.heap[0];
        else return undefined;
    }

    public push(node: T): void {
        this.heap.push(node);
        this.bubbleUp();
    }

    public pop(): T | undefined {
        if (this.length === 0) {
            return undefined;
        }
        [this.heap[0], this.heap[this.length - 1]] = [
            this.heap[this.length - 1],
            this.heap[0],
        ];
        const pop = this.heap.pop();
        this.bubbleDown();
        return pop;
    }

    private bubbleUp(): void {
        let current = this.length - 1;
        while (current > 0) {
            let parent = Math.ceil(current / 2) - 1;
            if (this.compare(this.heap[current], this.heap[parent]) == 1) {
                [this.heap[current], this.heap[parent]] = [
                    this.heap[parent],
                    this.heap[current],
                ];
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
            let bigger: number;
            if (this.compare(this.heap[left], this.heap[right]) == 1) {
                bigger = left;
            } else {
                bigger = right;
            }
            if (this.compare(this.heap[bigger], this.heap[current]) == 1) {
                [this.heap[bigger], this.heap[current]] = [
                    this.heap[current],
                    this.heap[bigger],
                ];
                current = bigger;
            } else {
                return;
            }
        }
    }
}

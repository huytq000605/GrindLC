class MinStack {
    arr
    min
    constructor() {
        this.min = []
        this.arr = []
    }

    push(val: number): void {
        this.arr.push(val)
        if(!this.min.length) this.min.push(val)
        else this.min.push(Math.min(val, this.min[this.min.length - 1]))
    }

    pop(): void {
        this.arr.pop()
        this.min.pop()
    }

    top(): number {
        return this.arr[this.arr.length - 1]
    }

    getMin(): number {
        return this.min[this.min.length - 1]
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
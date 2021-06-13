class FrontMiddleBackQueue {
    queue: number[]
    constructor() {
        this.queue = []
    }

    pushFront(val: number): void {
        this.queue.unshift(val)

    }

    pushMiddle(val: number): void {
        const middle = Math.floor(this.queue.length / 2);
        this.queue = [...this.queue.slice(0, middle), val, ...this.queue.slice(middle)]
        
    }

    pushBack(val: number): void {
        this.queue.push(val)
    }

    popFront(): number {
        if(!this.queue.length) return -1
        return this.queue.shift()
    }

    popMiddle(): number {
        if(!this.queue.length) return -1
        const middle = this.queue.length % 2 == 1 ? Math.floor(this.queue.length/ 2) : Math.floor(this.queue.length/2)-1;
        const result = this.queue[middle]
        this.queue = [...this.queue.slice(0, middle), ...this.queue.slice(middle + 1)]
        return result
    }

    popBack(): number {
        if(!this.queue.length) return -1
        return this.queue.pop()
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = new FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */